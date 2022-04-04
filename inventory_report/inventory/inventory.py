import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @classmethod
    def import_data(cls, path, relatorio: str) -> str:
        lista = cls.read(path)
        result_report = ""
        if relatorio == "simples":
            result_report = SimpleReport.generate(lista)
        elif relatorio == "completo":
            result_report = CompleteReport.generate(lista)
        else:
            raise Exception("Opção inválida")
        return result_report

    @staticmethod
    def read(path) -> list[dict]:
        list_of_file = []
        with open(path) as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in file_reader:
                list_of_file.append(row)
            return list_of_file
