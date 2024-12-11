from datetime import datetime

def log(output: str):
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {output}")

def error(output: str):
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {output}")