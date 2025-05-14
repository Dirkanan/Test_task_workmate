"""
Тесты для фабрики отчетов.
"""

import pytest
from utils.report_builder import ReportBuilder
from utils.report import SalaryPaymentReport

def test_factory_creates_correct_report_type():
    """Проверка создания правильного типа отчета"""
    report_instance = ReportBuilder.create_report("payout")
    assert isinstance(report_instance, SalaryPaymentReport)

def test_factory_with_invalid_report_type():
    """Проверка обработки неверного типа отчета"""
    with pytest.raises(ValueError) as error_info:
        ReportBuilder.create_report("invalid_type")
    assert "Unknown report type" in str(error_info.value)