import json
import os
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    def import_data(path):
        # https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
        file, ext = os.path.splitext(path)
        if ext == ".json":
            with open(path) as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
