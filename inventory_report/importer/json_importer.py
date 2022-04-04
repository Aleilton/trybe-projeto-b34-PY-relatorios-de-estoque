from typing import List, Dict
import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    def import_data(path) -> List[Dict]:
        ext = path.split(".")[-1]
        if ext == "json":
            with open(path) as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
