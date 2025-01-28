import os
from pathlib import Path
import shutil
import zipfile
from picsellia import DatasetVersion
from picsellia.sdk.dataset_version import MultiAsset
from picsellia.types.enums import AnnotationFileType

from common.logs import log, error

def download_assets(assets: MultiAsset, path: str):
	assets.download(path, use_id=True)
	log(f"Downloaded assets to {path}")

def download_annotations(dataset: DatasetVersion, path: str):
	try:
		path_to_annotation_zip: Path = Path(dataset.export_annotation_file(AnnotationFileType.YOLO, "./", use_id=True))

		if not zipfile.is_zipfile(path_to_annotation_zip):
			raise Exception(f"The file {path_to_annotation_zip} is not a zip file")
		with zipfile.ZipFile(path_to_annotation_zip, "r") as zip_ref:
			os.makedirs(path, exist_ok=True)
			zip_ref.extractall(path)
			print(f"Annotations extracted to {os.path.abspath(path)}")
		directory_to_remove = path_to_annotation_zip.parent.parent
		shutil.rmtree(directory_to_remove)

	except Exception as e:
		error(e, True)
	else:
		log(f"Downloaded annotations to {path}")

def split_annotations(path_to_assets, path_to_annotations): # a verifier
	for root, dirs, files in os.walk(path_to_assets):
		for file in files:
			if file.endswith(".jpg"):
				annotation_file = file.replace(".jpg", ".txt")
				annotation_path = os.path.join(root, annotation_file)
				if os.path.exists(annotation_path):
					annotation_folder = os.path.join(path_to_annotations, os.path.basename(root))
					os.makedirs(annotation_folder, exist_ok=True)
					shutil.move(annotation_path, annotation_folder)
					log(f"Moved {annotation_file} to {annotation_folder}")
				else:
					error(f"Annotation file {annotation_file} not found", True)