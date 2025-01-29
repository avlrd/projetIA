from picsellia import Experiment
from picsellia.sdk.dataset_version import MultiAsset

from data.config import Config
from data.preparation import download_assets, download_annotations, bind_annotations

data_path: str = "./.data"
assets_path: str = data_path + "/assets"
annotations_path: str = data_path + "/annotations"
train_path: str = "/train"
test_path: str = "/test"
val_path: str = "/val"

config: Config = Config()

experiment: Experiment = config.get_experiment()

train_assets: MultiAsset = None
test_assets: MultiAsset = None
val_assets: MultiAsset = None
count_train: int = 0
count_test: int = 0
count_val: int = 0
labels: list = []

train_assets, test_assets, val_assets, count_train, count_test, count_val, labels = config.get_dataset().train_test_val_split([60.0, 20.0, 20.0], 42, 250)

download_assets(train_assets, assets_path + train_path)
download_assets(test_assets, assets_path + test_path)
download_assets(val_assets, assets_path + val_path)

download_annotations(config.get_dataset(), annotations_path)

bind_annotations(assets_path, annotations_path)

#Pre-processing

	# config ultralytics

		# fichier yaml comme suit :
		# train: path
		# val: path
		# test: path
		#
		# nc: x (nombre de classes)
		# names: ['', '', '', ...] # liste des classes

	# Choisir les augmentations pertinentes et les mettre en place


# Training du modèle

	# Config des hyper-params -> meilleurs perfs (close_mosaic = 0 et seed = 42)

	# Archi YOLOv11, version à décider

	# Générer les métriques tout au long du training , accessibles via des callbacks et les log en temps réel sur Picsellia


# Evaluation du modèle

	# best.pt -> évaluer ses perfs avec ultralytics, log les métriques calculées sur Picsellia dans l'exp créée au début

	# Log chaque image du split de test dans l'onglet évaluation pour comparer y_pred et y_true

	# stocker le modèle entrainé dans un model_version

print("\nProgram ended successfully")