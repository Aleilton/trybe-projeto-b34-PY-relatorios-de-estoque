import os
import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    def import_data(path):
        # https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
        file, ext = os.path.splitext(path)
        if ext == ".xml":
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
