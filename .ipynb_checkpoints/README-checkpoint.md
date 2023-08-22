# JobFinder
Une application web qui conseillera un utilisateur en lui proposant des jobs qui lui correspondent

Code couleurs de l'application : 
- SEIGNEURIE bleu banten #294E54
- Bleu d'eau RAL 5021 #00747d
- couleur textes : #F0F0F2
- couleur titres : #ffffff

# Input du modèle : 

- job
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