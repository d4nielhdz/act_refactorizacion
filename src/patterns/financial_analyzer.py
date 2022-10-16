from patterns import csv_utils
from patterns.print_report import PrintReport
from patterns.web_report import WebReport


class FinancialAnalyzer():
    def __init__(self):
        self.financial_report_controller = FinancialReportController()
        
    def get_data(self, src):
        self.data = csv_utils.parse_file(src)

    def create_report(self, type):
        self.financial_report_controller.set_report_type(type)
        self.financial_report_controller.create_report(self.data)


class FinancialReportController:
    def set_report_type(self, type):
        # SIMPLE FACTORY
        if type == "web":
            self.reporter = WebReport()
        elif type == "print":
            self.reporter = PrintReport()


    def create_report(self, data):
        # ADAPTER -- LISKOV SUBSTITUTION PRINCIPLE
        self.reporter.create_report(data)