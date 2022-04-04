import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    def import_data(path) -> list[dict]:
        ext = path.split(".")[-1]
        if ext == "xml":
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
