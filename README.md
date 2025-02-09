# Projet IA

## How to
### English

- Create a .env file at the root of the program (where main.py is) :

```.env
# Picsellia config
API_TOKEN=
ORG_NAME=Picsalex-MLOps
PROJECT_ID=
DATASET_ID=
EXPERIMENT_NAME=
MODEL_ID=

# Path config
DATA_PATH=
HPCONFIG_FILE_PATH=
```

- Choose an experiment name for your new experiment
- Fill the variables with your tokens from Picsellia and paths to resources
- Configure hyper parameters in a yaml file which path you will need to specify in the .env file
- Run ```python main.py```

For the inference:

- Start program detectiondedouceur.py
- Choose mode
- Choose a model from the list

### Français

- Créez un fichier .env à la racine du programme (où se trouve le fichier main.py) :

```.env
# Picsellia config
API_TOKEN=
ORG_NAME=Picsalex-MLOps
PROJECT_ID=
DATASET_ID=
EXPERIMENT_NAME=
MODEL_ID=

# Path config
DATA_PATH=
HPCONFIG_FILE_PATH=
```

- Choisissez un nom pour la nouvelle "experiment"
- Remplissez les variables avec vos tokens Picsellia puis les chemins vers vos ressources
- Configurez les hyper parametres via un fichier yaml, dont vous préciserez le chemin d'accès dans le fichier .env
- Exécutez la commande : ```python main.py```

Pour l'inférence :

- Lancez le programme detectiondedouceur.py
- Choisissez le mode
- Choisissez le model d'après la liste affichée

## Authors

Younes BOKHARI  
Alexandre ROBERT  
Arthur VILLARD  
