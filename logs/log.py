from datetime import datetime

def log(output):
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {output}")