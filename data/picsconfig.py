from picsellia import Client, Project, DatasetVersion, Experiment, Model
from decouple import config, UndefinedValueError

from common.logs import log, error

class PicsConfig:
	def __init__(self):
		try:
			self.__client: Client = Client(
				api_token=config("API_TOKEN"),
				organization_name=config("ORG_NAME")
			)

			self.__project_id: 			str = config("PROJECT_ID")
			self.__dataset_id: 			str = config("DATASET_ID")
			self.__model_id: 			str = config("MODEL_ID")
			self.__experiment_name: 	str = config("EXPERIMENT_NAME")

			self.__project: Project = self.__client.get_project_by_id(self.__project_id)

		except UndefinedValueError as e:
			error(e, True)
		
		else:
			log("Config loaded")

	def get_dataset(self) -> DatasetVersion:
		return self.__client.get_dataset_version_by_id(self.__dataset_id)

	def get_experiment(self) -> Experiment:
		if(self.__project.get_experiment(self.__experiment_name) is not None):
			old_experiment: Experiment = self.__project.get_experiment(self.__experiment_name)
			old_experiment.delete()
		experiment: Experiment = self.__project.create_experiment(self.__experiment_name)
		experiment.attach_dataset("Dataset", self.get_dataset())
		return experiment
	
	def get_model(self) -> Model:
		return self.__client.get_model_by_id(self.__model_id)
