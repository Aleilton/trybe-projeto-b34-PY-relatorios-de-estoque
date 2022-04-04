from datetime import datetime


class SimpleReport:

    @classmethod
    def generate(cls, lista: list) -> str:
        return (
            f"{cls.oldest_manufacturing_date(lista)}\n"
            f"{cls.closest_expiration_date(lista)}\n"
            f"{cls.company_stocked_products(lista)}\n"
        )

    @classmethod
    def oldest_manufacturing_date(cls, lista: list) -> str:
        oldest_dates = set()
        for item in lista:
            oldest_dates.add(item["data_de_fabricacao"])
        return (f"Data de fabricação mais antiga: {sorted(oldest_dates)[0]}")

    @classmethod
    def closest_expiration_date(cls, lista: list) -> str:
        closest_dates = set()
        for item in lista:
            item_data = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            if item_data > datetime.now():
                closest_dates.add(item["data_de_validade"])
        return (f"Data de validade mais próxima: {sorted(closest_dates)[0]}")

    @classmethod
    def company_stocked_products(cls, lista: list) -> str:
        result = {}
        for item in lista:
            company = item["nome_da_empresa"]
            if company not in result:
                result[company] = 0
            result[company] += 1
        return (
            "Empresa com maior quantidade de produtos estocados: "
            f"{sorted(result)[-1]}"
        )
