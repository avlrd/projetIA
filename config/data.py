import os
from picsellia import Client, DatasetVersion, Project, Experiment, Asset
from dotenv import load_dotenv
import logging

from logs.log import *

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

try:
	if not load_dotenv():
		raise FileNotFoundError("Environment file not found. Please check that .env file exists in the project.")
	
	api_token = os.getenv("API_TOKEN")
	if not api_token:
		raise ValueError("Missing environment variable: API_TOKEN.")

except FileNotFoundError as e:
	error(e)
except ValueError as e:
	error(e)

project_id = "01936421-2de9-7259-8a28-c059512eb2fb"
dataset_id = "0193688e-aa8f-7cbe-9396-bec740a262d0"

client: Client = Client(
	api_token=api_token,
	organization_name="Picsalex-MLOps",
	host="https://app.picsellia.com"
)

project: Project = client.get_project_by_id("01936421-2de9-7259-8a28-c059512eb2fb")
dataset: DatasetVersion = client.get_dataset_version_by_id("0193688e-aa8f-7cbe-9396-bec740a262d0")

log(f"Loaded project [{project.name}] and attached dataset [{dataset.name}] version [{dataset.version}]")

# Créer une nouvelle experience
new_experiment = project.create_experiment("Test 1", "Experiment de test n°1")
new_experiment.attach_dataset("test_dataset", dataset)

# dl les images
## assets = dataset.list_assets() # type Multiasset non importable ??
## assets.download("./assets/")
## log("Downloaded all assets from dataset")

# dl les annotations au format YOLO pour ultralytics