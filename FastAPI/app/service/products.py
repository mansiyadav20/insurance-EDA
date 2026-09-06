import json
from typing import List,Dict
from pathlib import Path

Data_file=Path("..","data","products.json")

def load_products()->List[Dict]:
    if not Data_file.exists():
        return []
    with open(Data_file,"r",encoding="utf-8") as file:
        return json.load(file)

def get_all_products()->List[Dict]:
    return load_products()