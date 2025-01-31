import yaml
from ultralytics import YOLO

def start_training() -> None:
	model = YOLO("yolo11n.pt")

	# see best way to open local yaml and if not exist -> default

	model.train(
		data=f"./.data/data.yaml",
		epochs=100,
		patience=10,
		batch=16,
		imgsz=640,
		device="0",
		workers=8,
		exist_ok=True,
		optimizer="AdamW",
		seed=42,
		close_mosaic=0,
		lr0=0.001
	)