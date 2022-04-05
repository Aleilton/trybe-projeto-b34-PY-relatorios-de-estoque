import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        ext = (sys.argv[1]).split(".")[-1]
        if ext.lower() == "csv":
            instance = InventoryRefactor(CsvImporter)
        elif ext.lower() == "json":
            instance = InventoryRefactor(JsonImporter)
        elif ext.lower() == "xml":
            instance = InventoryRefactor(XmlImporter)
        else:
            raise ValueError("Arquivo inválido")
        data_result = instance.import_data(sys.argv[1], sys.argv[2])
        print(data_result, end='')
