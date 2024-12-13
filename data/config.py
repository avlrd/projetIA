from picsellia import Client, Project
from decouple import config, UndefinedValueError

from common.logs import *

try:
	client: Client = Client(
		api_token=config("API_TOKEN"),
		organization_name=config("ORG_NAME"),
		host=config("HOST")
	)

	project_id: str = config("PROJECT_ID")
	dataset_id: str = config("DATASET_ID")
	experiment_name: str = config("EXPERIMENT_NAME")
	path_to_assets: str = config("ASSETS")
	path_to_annotations: str = config("ANNOTATIONS")

	project: Project = client.get_project_by_id(project_id)

except UndefinedValueError as e:
	error(e, True)

else:
	log("Config loaded")