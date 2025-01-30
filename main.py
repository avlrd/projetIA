from picsellia import Experiment
from picsellia.sdk.dataset_version import MultiAsset
from ultralytics import YOLO

from data.picsconfig import PicsConfig
from data.preparation import download_assets, download_annotations, bind_annotations, config_data

if __name__ == "__main__":

	data_path: str = "./.data"
	assets_path: str = data_path + "/images"
	annotations_path: str = data_path + "/labels"
	train_path: str = "/train"
	test_path: str = "/test"
	val_path: str = "/val"

	config: PicsConfig = PicsConfig()

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

	config_data(data_path, labels)

	model = YOLO("yolo11n.pt")

	model.train(
		data=f"{data_path}/data.yaml",
		epochs=100,
		patience=10,
		batch=16,
		imgsz=640,
		device="0",
		workers=8,
		exist_ok=True,
		optimizer="AdamW",
		seed=42,
		close_mosaic=0,
		lr0=0.001
	)

# Choisir les augmentations pertinentes et les mettre en place


# Générer les métriques tout au long du training , accessibles via des callbacks et les log en temps réel sur Picsellia


# Evaluation du modèle

	# best.pt -> évaluer ses perfs avec ultralytics, log les métriques calculées sur Picsellia dans l'exp créée au début

	# Log chaque image du split de test dans l'onglet évaluation pour comparer y_pred et y_true

	# stocker le modèle entrainé dans un model_version

	print("\nProgram ended successfully")