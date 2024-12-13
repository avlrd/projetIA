import os
from picsellia import DatasetVersion
from picsellia.types.enums import AnnotationFileType
from picsellia.sdk.asset import MultiAsset
import zipfile
import shutil

from common.logs import *

from data.config import *

# s'arrêter la pour l'instant
exit(0)

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################


dataset: DatasetVersion = client.get_dataset_version_by_id("0193688e-aa8f-7cbe-9396-bec740a262d0")

old_experiment = project.get_experiment(experiment_name)
old_experiment.delete()
new_experiment = project.create_experiment(experiment_name, "Experiment de test n°1")
new_experiment.attach_dataset("test_dataset", dataset)

assets: MultiAsset = dataset.list_assets()
# assets.download(path_to_assets, use_id=True)

path_to_annotation_zip: str = dataset.export_annotation_file(AnnotationFileType.YOLO, "./", use_id=True)

try:
	if not zipfile.is_zipfile(path_to_annotation_zip):
		raise Exception(f"The file {path_to_annotation_zip} is not a zip file")
	with zipfile.ZipFile(path_to_annotation_zip, "r") as zip_ref:
		os.makedirs(path_to_annotations, exist_ok=True)
		zip_ref.extractall(path_to_annotations)
		print(f"Annotations extracted to {os.path.abspath(path_to_annotations)}")
		# attention les yeux
		directory_to_remove = os.path.dirname(os.path.dirname(path_to_annotation_zip))
		shutil.rmtree(directory_to_remove)
except Exception as e:
	print(e)
	exit(1)


#Pre-processing

    # Split 60 20 20 seed 42

    # Vérifier la structure du dataset

    # config ultralytics

		# fichier yaml comme suit :
		# train: path
		# val: path
		# test: path
		#
		# nc: x (nombre de classes)
		# names: ['', '', '', ...] # liste des classes


# Training du modèle

    # Config des hyper-params -> meilleurs perfs (close_mosaic = 0 et seed = 42)

    # Archi YOLOv11, version à décider

    # Générer les métriques tout au long du training , accessibles via des callbacks et les log en temps réel sur Picsellia


# Evaluation du modèle

    # best.pt -> évaluer ses perfs avec ultralytics, log les métriques calculées sur Picsellia dans l'exp créée au début

    # Log chaque image du split de test dans l'onglet évaluation pour comparer y_pred et y_true

    # stocker le modèle entrainé dans un model_version

print("\nProgram ended successfully")