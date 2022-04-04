import os
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @classmethod
    def import_data(cls, path, relatorio: str) -> str:
        lista = cls.get_lista_by_type_file(path)
        if relatorio == "simples":
            result_report = SimpleReport.generate(lista)
        elif relatorio == "completo":
            result_report = CompleteReport.generate(lista)
        else:
            raise Exception("Opção inválida")
        return result_report

    @staticmethod
    def get_lista_by_type_file(path) -> list[dict]:
        # https://www.horadecodar.com.br/2021/04/17/extrair-extensao-do-arquivo-com-python/
        file, ext = os.path.splitext(path)
        if ext.lower() == ".csv":
            lista = CsvImporter.import_data(path)
        elif ext.lower() == ".json":
            lista = JsonImporter.import_data(path)
        elif ext.lower() == ".xml":
            lista = XmlImporter.import_data(path)
        else:
            raise ValueError("Arquivo inválido")
        return lista
