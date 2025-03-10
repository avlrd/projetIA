import os
import yaml
from pathlib import Path
import shutil
import zipfile
from picsellia import DatasetVersion
from picsellia.sdk.dataset_version import MultiAsset
from picsellia.types.enums import AnnotationFileType

from common.logs import log, error

def download_assets(assets: MultiAsset, path: str) -> None:
	assets.download(path, use_id=True)
	log(f"Downloaded assets to {path}")

def download_annotations(dataset: DatasetVersion, path: str) -> None:
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

def bind_annotations(assets_path, annotations_path) -> None:
	try:
		for dirname in ['test', 'train', 'val']:
			os.makedirs(f"{annotations_path}/{dirname}", exist_ok=True)
			for asset in os.listdir(f"{assets_path}/{dirname}"):
				asset_id = os.path.splitext(asset)[0]
				annotation_path = f"{annotations_path}/{asset_id}.txt"
				if os.path.exists(annotation_path):
					shutil.move(annotation_path, f"{annotations_path}/{dirname}/{asset_id}.txt")
		os.remove(f"{annotations_path}/data.yaml")
	except Exception as e:
		error(e, True)
	else:
		log("Successfully binded annotations")

def config_data(data_path, labels) -> None:
	index: int = 0
	labels2 = {}
	for label in labels:
		labels2[index] = label.name
		index += 1

	try:
		yaml.dump({
			"path": data_path,
			"train": "images/train",
			"val": "images/val",
			"test": "images/test",
			"names": labels2
		}, open(f"{data_path}/data.yaml", "w"), default_flow_style=False)
		
	except Exception as e:
		error(e, True)
	else:
		log("Successfully configured data")
