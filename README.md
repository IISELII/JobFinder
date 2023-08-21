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

- job
- description de ce job (pas l'offre d'emploi mais plutôt un résumé de ce que fait le job en particulier. Je peux soit utiliser un Transformers soit la table job_salary)
- Les colonne job et lien de toutes les offres d'emploi de ce job qui datent de moins de 7 jours.

Exemple d'une séquence envoyé au modèle: [job]