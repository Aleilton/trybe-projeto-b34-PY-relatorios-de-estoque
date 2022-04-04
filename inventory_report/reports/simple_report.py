from datetime import datetime


class SimpleReport:

    @classmethod
    def generate(cls, lista):
        return (
            "Data de fabricação mais antiga: "
            f"{cls.oldest_manufacturing_date(lista)}\n"
            "Data de validade mais próxima: "
            f"{cls.closest_expiration_date(lista)}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{sorted(cls.company_stocked_products(lista))[-1]}\n"
        )

    @staticmethod
    def oldest_manufacturing_date(lista):
        oldest_dates = set()
        for item in lista:
            oldest_dates.add(item["data_de_fabricacao"])
        return sorted(oldest_dates)[0]

    @staticmethod
    def closest_expiration_date(lista):
        closest_dates = set()
        for item in lista:
            item_data = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            if item_data > datetime.now():
                closest_dates.add(item["data_de_validade"])
        return sorted(closest_dates)[0]

    @staticmethod
    def company_stocked_products(lista):
        result = {}
        for item in lista:
            company = item["nome_da_empresa"]
            if company not in result:
                result[company] = 0
            result[company] += 1
        return result
