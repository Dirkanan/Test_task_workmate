"""
Главный модуль для генерации отчетов по зарплатам.
Обрабатывает CSV файлы с данными сотрудников и создает отчеты.
"""

import argparse
from utils.employee_data_processor import CSVStaffDataReader
from utils.report_builder import ReportBuilder


def setup_arguments():
    """Настройка и парсинг аргументов командной строки"""
    arg_parser = argparse.ArgumentParser(
        description="Генератор финансовых отчетов для сотрудников")
    arg_parser.add_argument(
        "input_files",
        nargs="+",
        help="Файлы CSV с данными персонала")
    arg_parser.add_argument(
        "--report",
        required=True,
        choices=["payout"],
        help="Тип формируемого отчета")
    return arg_parser.parse_args()


def execute():
    """Основная логика программы"""
    cli_args = setup_arguments()
    staff_records = []

    for input_file in cli_args.input_files:
        data_processor = CSVStaffDataReader(input_file)
        staff_records.extend(data_processor.process())

    report = ReportBuilder.create_report(cli_args.report)
    report.build(staff_records)


if __name__ == "__main__":
    execute()