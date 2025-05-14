"""
Модуль для генерации различных типов отчетов по данным сотрудников.
"""

from abc import ABC, abstractmethod
from collections import defaultdict


class BaseReport(ABC):
    """Абстрактный базовый класс для отчетов"""

    @abstractmethod
    def build(self, employee_data: list[dict]) -> None:
        """Метод построения отчета"""
        pass


class SalaryPaymentReport(BaseReport):
    """Отчет по выплатам зарплат с группировкой по отделам"""

    def build(self, employee_data: list[dict]) -> None:
        """Генерация отчета о выплатах"""
        # Настройки форматирования вывода
        output_format = {
            "name": 18,
            "hours": 7,
            "rate": 6,
            "payout": 9,
        }

        # Заголовок отчета
        report_header = (
            f'{"":18}'
            f'{"name":{output_format["name"]}}'
            f'{"hours":>{output_format["hours"]}}'
            f'{"rate":>{output_format["rate"]}}'
            f'{"payout":>{output_format["payout"]}}'
        )
        print(report_header)

        # Группировка сотрудников по отделам
        department_groups = defaultdict(list)
        for employee in employee_data:
            department_groups[employee["department"]].append(employee)

        # Вывод данных по каждому отделу
        for department, staff in department_groups.items():
            print(f"\n{department}")
            department_hours = 0
            department_total = 0

            for person in staff:
                salary = person["hours"] * person["rate"]
                department_hours += person["hours"]
                department_total += salary

                print(
                    f'{"-" * 15} '
                    f'{person["name"]:<{output_format["name"]}}'
                    f'{person["hours"]:>{output_format["hours"]}}'
                    f'{person["rate"]:>{output_format["rate"]}}'
                    f'${salary:>{output_format["payout"]}}$'
                )

            # Итоговая строка по отделу
            print(
                f'{" " * 15} '
                f'{" ":{output_format["name"]}}'
                f'{department_hours:>{output_format["hours"]}}'
                f'{" ":{output_format["rate"] + 1}}'
                f'{department_total:>{output_format["payout"]}}$'
            )