"""
Модуль для чтения и обработки данных сотрудников из CSV файлов.
Поддерживает различные форматы входных данных.
"""

from abc import ABC, abstractmethod


class BaseDataReader(ABC):
    """Абстрактный базовый класс для чтения данных"""

    @abstractmethod
    def process(self) -> list[dict]:
        """Основной метод обработки данных"""
        pass


class CSVStaffDataReader(BaseDataReader):
    """Реализация чтения данных персонала из CSV"""

    def __init__(self, file_path: str):
        """Инициализация с указанием пути к файлу"""
        self.data_file = file_path

    def process(self) -> list[dict]:
        """Обработка CSV файла и преобразование в структурированные данные"""
        with open(self.data_file, encoding="utf-8") as data_stream:
            # Подготовка заголовков и сопоставление колонок
            columns = data_stream.readline().strip().split(",")
            column_mapping = {
                "name": "employee_name",
                "department": "division",
                "hours_worked": "work_hours",
                "hours": "work_hours",
                "hourly_rate": "pay_rate",
                "rate": "pay_rate",
                "salary": "pay_rate",
            }

            # Создание индексов для нужных колонок
            column_indexes = {
                column_mapping.get(col, col): idx
                for idx, col in enumerate(columns)
                if column_mapping.get(col, col) in {
                    "employee_name", "division", "work_hours", "pay_rate"
                }
            }

            processed_data = []
            for record_line in data_stream:
                if not record_line.strip():
                    continue

                values = record_line.strip().split(",")
                processed_data.append({
                    "name": values[column_indexes["employee_name"]],
                    "department": values[column_indexes["division"]],
                    "hours": int(values[column_indexes["work_hours"]]),
                    "rate": int(values[column_indexes["pay_rate"]]),
                })

            return processed_data