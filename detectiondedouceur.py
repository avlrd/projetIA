# load le modele avec ultralytics
# faire une inférence avec trois modes possibles : IMAGE, VIDEO, WEBCAM

import sys
import os
from ultralytics import YOLO
from picsellia import Model, ModelVersion, ModelFile

from data.picsconfig import PicsConfig

### METHODS

def print_usage() -> None:
	print("Usage: python detectiondedouceur.py [IMAGE|VIDEO|WEBCAM] --path <path> (if WEBCAM is chosen, no need to specify path)")

def ask_for_mode() -> str:
	choices: list[str] = ["IMAGE", "VIDEO", "WEBCAM"]
	mode: str = input("Choose mode (IMAGE, VIDEO, WEBCAM): ")
	if mode not in choices:
		print("Error: Invalid mode")
		return ask_for_mode()
	return mode

def get_path() -> str:
	path: str = input("Enter path to file: ")
	if not os.path.exists(path):
		print(f"Error: File {path} does not exist")
		return get_path()
	return path

def get_args() -> tuple[str, str]:
	mode: str = ask_for_mode()
	if mode in ["IMAGE", "VIDEO"]:
		path: str = get_path()
		return mode, path
	else:
		return mode, None
	
def ask_for_version(model: Model) -> str:
	model_versions: list[ModelVersion] = model.list_versions()
	print("Available versions:")
	for model_version in model_versions:
		print(model_version.name)
	version: str = input("Choose model version: ")

	if version not in [model_version.name for model_version in model_versions]:
		print(f"Error: Model version {version} does not exist")
		return ask_for_version(model)
	return version

###

### SCRIPT

mode, path = get_args()

config: PicsConfig = PicsConfig()

project_model: Model = config.get_model()

version: str = ask_for_version(project_model)

model_version: ModelVersion = project_model.get_version(version)
file: ModelFile = model_version.get_file("model-best")
file.download()

model = YOLO("./best.pt")

match mode:
	case "IMAGE" | "VIDEO":
		result = model(path, device="cuda", show=True)

	case "WEBCAM":
		result = model(0, device="cuda", show=True)
	case _:
		print("Error: Invalid mode, shouldn't happen")
		sys.exit(1)

###