import json
from typing import List, Dict

def read_data(filename: str) -> List[Dict]:
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_data(filename: str, data: List[Dict]):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
