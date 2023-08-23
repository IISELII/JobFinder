# JobFinder
Une application web qui conseillera un utilisateur en lui proposant des jobs qui lui correspondent

Code couleurs de l'application : 
- SEIGNEURIE bleu banten #294E54
- Bleu d'eau RAL 5021 #00747d
- couleur textes : #F0F0F2
- couleur titres : #ffffff

# Input du modèle : 

- description
- tools
- secteur / Industrie

Exemple d'une séquence envoyé au modèle: [[description], [tools], [industry]]

# Target du modèle : 

- job : le titre du job
- job_description : description de ce job (pas l'offre d'emploi mais plutôt un résumé de ce que fait le job en particulier. Je peux soit utiliser un Transformers soit la table job_salary)
- link : Les colonne job et lien de toutes les offres d'emploi de ce job qui datent de moins de 7 jours.

Exemple d'une séquence envoyé au modèle: [job, job_description, link]

# Comment avoir accès à la target job_description

La target job_description (la description du job) est légèrement différente de la colonne description (qui contient la description de l'offre d'emploi).
C'est une colonne qu'on ne possède pas au départ et qu'on aimerait créer, mais comment faire ?
Plusieurs solutions possible, la première :  

- utiliser un modèle IA pour extraire les bon nom de job (ex:Data Engineer pour la Qualité Totale H/F (H/F) --> Data Engineer)
- maintenant qu'on a les bon noms de job, séparer les descriptions (description de l'offre d'emploi) dans des listes différentes en fonction du job, puis les envoyer au modèle pour qu'il nous en ressort une description pour ce job.
- Quand tous les jobs seront fait, on aura un dataframe "jobdesc_df" qui aura deux colonnes "jobs, job_description". On mergera ce dataframe avec le dataframe principale et on aura donc accès à la target job_description.

La deuxième solution : 

- utiliser un modèle IA pour extraire les bon nom de job (ex:Data Engineer pour la Qualité Totale H/F (H/F) --> Data Engineer)
- maintenant qu'on a les bon noms de job, faire un df["jobs"].unique() et accéder à tout les noms de job, les envoyer à ChatGPT en lui demandant de nous faire une description de chaque job.
- mettre le résultat dans une liste qu'on transformera en dataframe et qu'on mergera au dataframe principale.

# Modèle d'IA pour extraire les bon noms de job

4 solutions potentielles : 

Approche basée sur les clustering :

- Les modèles comme BERT ou d'autres modèles d'embedding peuvent convertir vos titres en vecteurs. Vous pouvez ensuite utiliser une technique de clustering (comme le K-means) pour regrouper des titres similaires. Une fois les clusters formés, vous pouvez examiner manuellement les centres de clusters pour définir le titre représentatif de chaque cluster. Mais les clusters risque d'être trop vague et donc la prédiction ne sera pas assez précise.

En utilisant Regex ou Spacy :

- SpaCy est une bibliothèque populaire pour le traitement du langage naturel qui possède un modèle préentraîné pour la reconnaissance d'entités nommées en anglais (et d'autres langues). Bien que cela ne soit pas directement adapté à votre tâche, il est possible que le modèle puisse identifier les titres de poste comme des entités.

Zero-shot learning avec BERT :

- Bien que BERT soit principalement un modèle d'extraction de caractéristiques, vous pouvez l'utiliser pour des tâches de classification en zéro-shot. En gros, vous formulez votre tâche comme une tâche de similarité sémantique. Vous donnez à BERT une phrase comme "La tâche de ce poste est Data Engineer" et vous la comparez à vos titres. Le titre le plus similaire peut être considéré comme étant celui de "Data Engineer".

Utiliser un modèle de résumé automatique : 

- L'idée ici est un peu non conventionnelle, mais vous pourriez essayer d'utiliser un modèle de résumé pour résumer les titres de poste. Le modèle pourrait éliminer les informations non essentielles et conserver uniquement le titre du poste.

# Comment envoyer au modèle des une liste de description pour chaque job du df 

Le faire à la main est plutôt simple, mais l'automatiser est une necessitée en terme de temps et d'effort requis pour cette tâche, mais comment faire ? 

- Faire une fonction qui créer une liste de listes à partir du df (chaque sub_liste contiendra des description pour un job donné)
- Faire une fonction qui envoie au modèle cette liste de listes, le modèle prendra step by step chaque sub_liste et summarisera tous les texte de cette sub_liste en un seul text (la future description de ce job)
- au finale, la fonction renverra une liste de listes comme en input, mais cette fois ci chaque sub_liste ne contiendra qu'une seul description (la summarisation fait par le modèle et la futur colonne job_description)