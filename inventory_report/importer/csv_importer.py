import csv
import os
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    def import_data(path) -> list[dict]:
        list_of_file = []
        # https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
        file, ext = os.path.splitext(path)
        if ext == ".csv":
            with open(path) as file:
                file_read = csv.DictReader(file, delimiter=",", quotechar='"')
                for row in file_read:
                    list_of_file.append(row)
                return list_of_file
        else:
            raise ValueError("Arquivo inválido")
