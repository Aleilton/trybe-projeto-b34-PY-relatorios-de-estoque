from typing import List, Dict
import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    def import_data(path) -> List[Dict]:
        list_of_file = []
        ext = path.split(".")[-1]

        if ext == "csv":
            with open(path) as file:
                file_read = csv.DictReader(file, delimiter=",", quotechar='"')
                for row in file_read:
                    list_of_file.append(row)
                return list_of_file
        else:
            raise ValueError("Arquivo inválido")
