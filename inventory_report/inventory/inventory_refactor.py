from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):

    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, relatorio: str) -> str:
        self.data += self.importer.import_data(path)
        if relatorio == "simples":
            result_report = SimpleReport.generate(self.data)
        elif relatorio == "completo":
            result_report = CompleteReport.generate(self.data)
        else:
            raise Exception("Opção inválida")
        return result_report
