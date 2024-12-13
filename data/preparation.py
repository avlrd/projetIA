import os
from pathlib import Path
import shutil
import zipfile
from picsellia.sdk.dataset_version import MultiAsset
from picsellia.types.enums import AnnotationFileType

from data.config import *


try:
	assets: MultiAsset = dataset.list_assets()
	assets.download(path_to_assets, use_id=True)

	path_to_annotation_zip: Path = Path(dataset.export_annotation_file(AnnotationFileType.YOLO, "./", use_id=True))

	if not zipfile.is_zipfile(path_to_annotation_zip):
		raise Exception(f"The file {path_to_annotation_zip} is not a zip file")
	with zipfile.ZipFile(path_to_annotation_zip, "r") as zip_ref:
		os.makedirs(path_to_annotations, exist_ok=True)
		zip_ref.extractall(path_to_annotations)
		print(f"Annotations extracted to {os.path.abspath(path_to_annotations)}")
		directory_to_remove = path_to_annotation_zip.parent.parent
		shutil.rmtree(directory_to_remove)

	train_assets, test_assets, val_assets, count_train, count_test, count_val, labels = dataset.train_test_val_split([60, 20, 20], 42, 250)

except Exception as e:
	error(e)