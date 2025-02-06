from picsellia import Experiment, Model
from picsellia.sdk.dataset_version import MultiAsset
from decouple import config

from data.picsconfig import PicsConfig
from data.preparation import download_assets, download_annotations, bind_annotations, config_data
from training.training import start_training

if __name__ == "__main__":

	data_path: str = config("DATA_PATH", default="./.data")
	assets_path: str = data_path + "/images"
	annotations_path: str = data_path + "/labels"
	train_path: str = "/train"
	test_path: str = "/test"
	val_path: str = "/val"

	config: PicsConfig = PicsConfig()

	experiment: Experiment = config.get_experiment()
	model: Model = config.get_model()

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

	start_training(data_path, experiment, model)

	print("\nProgram ended successfully")