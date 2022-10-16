from patterns.financial_analyzer import FinancialAnalyzer

CSV_FILE = "taxi-data.csv"

def main():
    financial_data = FinancialAnalyzer()
    financial_data.get_data(CSV_FILE)

    financial_data.create_report("web")
    financial_data.create_report("print")


if __name__ == '__main__':
    main()
