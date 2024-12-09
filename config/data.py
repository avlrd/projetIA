from picsellia import Client, DatasetVersion, Project
from logs.log import log

api_token = "185e119a0205ca1a92bf65af09c0469eecca2500"
project_id = "01936421-2de9-7259-8a28-c059512eb2fb"
dataset_id = "0193688e-aa8f-7cbe-9396-bec740a262d0"

client: Client = Client(
	api_token=api_token,
	organization_name="Picsalex-MLOps",
	host="https://app.picsellia.com"
)

project: Project = client.get_project_by_id("01936421-2de9-7259-8a28-c059512eb2fb")

dataset: DatasetVersion = client.get_dataset_version_by_id("0193688e-aa8f-7cbe-9396-bec740a262d0")

# Créer une nouvelle experience 
# dl les annotations au format YOLO pour ultralytics


log(f"Loaded project [{project.name}] with dataset [{dataset.name}] version [{dataset.version}]")