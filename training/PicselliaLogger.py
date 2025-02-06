import time
from picsellia import Experiment, Model, ModelVersion
from picsellia.types.enums import LogType
from ultralytics.models.yolo.detect import DetectionTrainer

class PicselliaLogger():
	def __init__(self, experiment: Experiment):
		self.experiment = experiment
		self.epoch_start_time = None
		self.epoch_end_time = None

	def on_train_start(self, trainer: DetectionTrainer):
		self.total_start_time = time.time()
		self.experiment.log("Model", str(trainer.model), LogType.EVALUATION)

	def on_epoch_start(self):
		self.epoch_start_time = time.time()

	def on_epoch_end(self, trainer: DetectionTrainer):
		epoch_duration = time.time() - self.epoch_start_time if self.epoch_start_time else 0
		self.experiment.log("Epoch duration", epoch_duration, LogType.EVALUATION)

	def on_train_end(self, trainer: DetectionTrainer):
		total_duration = time.time() - self.total_start_time
		self.experiment.log("Total duration", total_duration, LogType.EVALUATION)

		self.experiment.log("Confusion matrix", trainer.metrics["confusion_matrix"], LogType.EVALUATION)
		self.experiment.log("Fitness", trainer.metrics["fitness"], LogType.EVALUATION)
		for data in trainer.metrics["results_dict"]:
			self.experiment.log(data, trainer.metrics["results_dict"][data], LogType.EVALUATION)

def save_model(experiment: Experiment, model: Model, trainer: DetectionTrainer):
	labels: dict = {index: label.name for index, label in enumerate(experiment.get_dataset("initial").list_labels())}

	model_version: ModelVersion = model.create_version(
		labels=labels,
		name=experiment.name,
		framework="pytorch",
		type="detection",
		description="Model for experiment " + experiment.name
	)

	model_version.store("model-best", trainer.best)
	