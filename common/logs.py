from datetime import datetime


def log(message: str):
	print(f'\033[32m[{datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}] {message}\033[0m')

def error(message: str, stop: bool):
	output: str = f'\033[31m[{datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}] - Error: {message}'
	output += " Exiting." if stop else " Continuing..."
	output += "\033[0m"
	print(output)
	if stop:
		exit(1)