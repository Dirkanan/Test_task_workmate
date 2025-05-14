"""
Фабрика для создания различных типов отчетов.
Позволяет легко добавлять новые виды отчетов.
"""

from .report import SalaryPaymentReport


class ReportBuilder:
    """Фабричный класс для генерации отчетов разных типов"""

    # Реестр доступных типов отчетов
    _registered_reports = {
        "payout": SalaryPaymentReport,
    }

    @classmethod
    def create_report(cls, report_type: str):
        """
        Создает экземпляр запрошенного типа отчета

        Args:
            report_type: Идентификатор типа отчета (например, "payout")

        Returns:
            Экземпляр класса отчета

        Raises:
            ValueError: Если запрошен неизвестный тип отчета
        """
        if report_type not in cls._registered_reports:
            raise ValueError(f"Unknown report type: {report_type}")

        return cls._registered_reports[report_type]()