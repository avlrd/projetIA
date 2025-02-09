import yaml
from ultralytics import YOLO
from decouple import config, UndefinedValueError
from picsellia import Experiment, Model

from training.PicselliaLogger import PicselliaLogger, save_model
from common.logs import error, log

def load_training_config() -> dict:
	try:
		hpconfig_file_path: str = config("HPCONFIG_FILE_PATH", default="./hpconfig_default.yaml")
		log(f"Loading hyperparameters from {hpconfig_file_path}")
		with open(hpconfig_file_path, "r") as file:
			hpconfig: dict = yaml.load(file, Loader=yaml.FullLoader)
	except UndefinedValueError as e:
		error(f"Error while loading .env file: {e}", True)
	except FileNotFoundError as e:
		error(f"File {hpconfig_file_path} not found: {e}", True)
	except yaml.YAMLError as e:
		error(f"Error while loading {hpconfig_file_path}: {e}", True)
	else:
		return hpconfig


def start_training(data_path: str, experiment: Experiment, picsmodel: Model) -> None:
	hpconfig: dict = load_training_config()

	model = YOLO(hpconfig["model"])

	logger: PicselliaLogger = PicselliaLogger(experiment)

	model.add_callback("on_train_start", logger.on_train_start)
	model.add_callback("on_train_epoch_end", logger.on_train_epoch_end)
	model.add_callback("on_train_end", logger.on_train_end)

	model.train(
		data=data_path+"/data.yaml",
		epochs=hpconfig["epochs"],
		patience=hpconfig["patience"],
		batch=hpconfig["batch"],
		imgsz=hpconfig["imgsz"],
		device=hpconfig["device"],
		workers=hpconfig["workers"],
		exist_ok=hpconfig["exist_ok"],
		optimizer=hpconfig["optimizer"],
		lr0=hpconfig["lr0"],
		cache=hpconfig["cache"],
		seed=42,
		close_mosaic=0,
		cos_lr=hpconfig["cos_lr"],
		flipud=hpconfig["flipud"],
		degrees=hpconfig["degrees"],
		perspective=hpconfig["perspective"],
		shear=hpconfig["shear"],
		hsv_h=hpconfig["hsv_h"]
	)

	save_model(experiment, picsmodel, model.trainer)
