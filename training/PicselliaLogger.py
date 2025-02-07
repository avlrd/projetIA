import time
from picsellia import Experiment, Model, ModelVersion
from picsellia.types.enums import LogType, InferenceType
from ultralytics.models.yolo.detect import DetectionTrainer

class PicselliaLogger():
	def __init__(self, experiment: Experiment):
		self.experiment = experiment

	def on_train_start(self, trainer: DetectionTrainer):
		self.experiment.log("Model", str(trainer.model), LogType.LINE)

	#def on_train_epoch_start(self, trainer: DetectionTrainer):
		

	def on_train_epoch_end(self, trainer: DetectionTrainer):
		# Here we log each value of the metrics object after each epoch
		# and it normally adds the value to the Log which is of type LINE
		# it should build a graph with the values of the metrics in real time
		# according to documentation
		for name, value in trainer.metrics.items():
			self.experiment.log(name, [value], LogType.LINE)
		self.experiment.log("Epoch duration", [trainer.epoch_time], LogType.BAR)
		self.experiment.log("Fitness", [trainer.fitness], LogType.LINE)
		if trainer.best_fitness is not None:
			self.experiment.log("Best fitness", trainer.best_fitness, LogType.VALUE)
		for index, loss_name in enumerate(trainer.loss_names):
			self.experiment.log(loss_name, [trainer.loss_items[index].item()], LogType.LINE)
			

	def on_train_end(self, trainer: DetectionTrainer):
		print(trainer.metrics)

def save_model(experiment: Experiment, model: Model, trainer: DetectionTrainer):
	labels: dict = {str(index): label.name for index, label in enumerate(experiment.get_dataset("Dataset").list_labels())}

	model_version: ModelVersion = model.create_version(
		labels=labels,
		name=experiment.name + time.strftime("-%Y-%m-%d-%H-%M-%S"),
		framework="pytorch",
		type=InferenceType.OBJECT_DETECTION,
		description="Best model for experiment " + experiment.name
	)

	model_version.store("model-best", trainer.best)
	