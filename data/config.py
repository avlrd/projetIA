from picsellia import Client, Project, DatasetVersion, Experiment
from decouple import config, UndefinedValueError

from common.logs import *

#################################################################
# Sets up everything from Picsellia to begin preparing data		#
#																#
# Exports:														#
# - path_to_assets												#
# - path_to_annotations											#
# - experiment													#
#################################################################

try:
	__client: Client = Client(
		api_token=config("API_TOKEN"),
		organization_name=config("ORG_NAME"),
		host=config("HOST")
	)

	__project_id: 			str = config("PROJECT_ID")
	__dataset_id: 			str = config("DATASET_ID")
	__experiment_name: 		str = config("EXPERIMENT_NAME")
	path_to_assets: 		str = config("ASSETS")
	path_to_annotations: 	str = config("ANNOTATIONS")

	__project: Project = __client.get_project_by_id(__project_id)

	dataset: DatasetVersion = __client.get_dataset_version_by_id(__dataset_id)

	__old_experiment: Experiment = __project.get_experiment(__experiment_name)
	__old_experiment.delete()
	__new_experiment: Experiment = __project.create_experiment(__experiment_name)
	__new_experiment.attach_dataset("Dataset", dataset)
	# Pourquoi faut il spécifier un name lorsqu'on associe un dataset à l'experiment, alors que ce dataset est déjà nommé ?
	experiment: Experiment = __new_experiment

except UndefinedValueError as e:
	error(e, True)

else:
	log("Config loaded")
