from typing import List, Dict
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    def import_data(path) -> List[Dict]:
        ext = path.split(".")[-1]
        if ext == "xml":
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
