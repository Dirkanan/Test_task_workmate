"""
Тесты для отчета по выплатам зарплат.
"""

import pytest
from utils.report import SalaryPaymentReport

def test_report_output_structure(capsys):
    """Проверка структуры вывода отчета"""
    test_data = [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
        {"name": "Jane", "department": "HR", "hours": 20, "rate": 200},
    ]
    report = SalaryPaymentReport()
    report.build(test_data)
    output = capsys.readouterr().out
    assert "IT" in output
    assert "HR" in output
    assert "100" in output
    assert "200" in output