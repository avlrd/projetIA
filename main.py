import os
from picsellia import Client, Project, DatasetVersion
from picsellia.types.enums import AnnotationFileType
from picsellia.sdk.asset import MultiAsset
from dotenv import load_dotenv
import zipfile
from datetime import datetime

def log(message: str):
	print(f"[{datetime.now}] {message}")

def error(message: str, exit: bool):
	print(f"\033[31m[{datetime.now}] - Error: {message}\033[0m")
	if exit:
		print("Exiting")
		exit(1)
	else:
		print("Continuing")


if not load_dotenv():
	error("Failed to load .env file", exit=True)

api_token: str = os.getenv("API_TOKEN")
if not api_token:
	error("API_TOKEN not found in .env file", exit=True)

project_id = "01936421-2de9-7259-8a28-c059512eb2fb"
dataset_id = "0193688e-aa8f-7cbe-9396-bec740a262d0"
path_to_assets = "./assets"
experiment_name = "Test"

client: Client = Client(
	api_token=api_token,
	organization_name="Picsalex-MLOps",
	host="https://app.picsellia.com"
)

project: Project = client.get_project_by_id(project_id)


#########################################################################################################################
#########################################################################################################################
#########################################################################################################################


dataset: DatasetVersion = client.get_dataset_version_by_id("0193688e-aa8f-7cbe-9396-bec740a262d0")

old_experiment = project.get_experiment(experiment_name)
old_experiment.delete()
new_experiment = project.create_experiment(experiment_name, "Experiment de test n°1")
new_experiment.attach_dataset("test_dataset", dataset)

assets: MultiAsset = dataset.list_assets()
assets.download(path_to_assets, use_id=True)

# dl les annotations au format YOLO pour ultralytics
path_to_annotations = "./annotations"
path_to_annotation_zip: str = dataset.export_annotation_file(AnnotationFileType.YOLO, "./", use_id=True)

try:
	if not zipfile.is_zipfile(path_to_annotation_zip):
		raise Exception(f"The file {path_to_annotation_zip} is not a zip file")
	with zipfile.ZipFile(path_to_annotation_zip, "r") as zip_ref:
		os.makedirs("./annotations", exist_ok=True)
		zip_ref.extractall("./annotations")
		print(f"Annotations extracted to {os.path.abspath('./annotations')}")
		os.rmdir(path_to_annotation_zip)
except Exception as e:
	print(e)
	exit(1)


#Pre-processing

    # Split 60 20 20 seed 42

    # Vérifier la structure du dataset

    # config ultralytics


# Training du modèle

    # Config des hyper-params -> meilleurs perfs (close_mosaic = 0 et seed = 42)

    # Archi YOLOv11, version à décider

    # Générer les métriques tout au long du training , accessibles via des callbacks et les log en temps réel sur Picsellia


# Evaluation du modèle

    # best.pt -> évaluer ses perfs avec ultralytics, log les métriques calculées sur Picsellia dans l'exp créée au début

    # Log chaque image du split de test dans l'onglet évaluation pour comparer y_pred et y_true

    # stocker le modèle entrainé dans un model_version

print("\nProgram ended successfully")