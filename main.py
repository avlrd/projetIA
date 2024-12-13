import data.preparation

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