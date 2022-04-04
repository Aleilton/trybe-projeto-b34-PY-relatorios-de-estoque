from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, lista: list) -> str:
        return (
            f"{super().generate(lista)}\n"
            "Produtos estocados por empresa: \n"
            f"{cls.company_stocked_products_list(lista)}"
        )

    @classmethod
    def company_stocked_products_list(cls, lista: list) -> str:
        companies = cls.company_stocked_products(lista)
        result = ""
        for company in companies.items():
            result += f"- {company[0]}: {company[1]}\n"
        return result
