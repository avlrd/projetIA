from picsellia import Client, Project, DatasetVersion, Experiment
from decouple import config, UndefinedValueError

from common.logs import log, error

class Config:
	def __init__(self):
		try:
			self.__client: Client = Client(
				api_token=config("API_TOKEN"),
				organization_name=config("ORG_NAME")
			)

			self.__project_id: 			str = config("PROJECT_ID")
			self.__dataset_id: 			str = config("DATASET_ID")
			self.__experiment_name: 	str = config("EXPERIMENT_NAME")

			self.__project: Project = self.__client.get_project_by_id(self.__project_id)

			self.__dataset: DatasetVersion = self.__client.get_dataset_version_by_id(self.__dataset_id)

			old_experiment: Experiment = self.__project.get_experiment(self.__experiment_name)
			old_experiment.delete()
			new_experiment: Experiment = self.__project.create_experiment(self.__experiment_name)
			new_experiment.attach_dataset("Dataset", self.__dataset)
			self.__experiment = new_experiment

		except UndefinedValueError as e:
			error(e, True)
		
		else:
			log("Config loaded")

	def get_dataset(self) -> DatasetVersion:
		return self.__dataset

	def get_experiment(self) -> Experiment:
		return self.__experiment
