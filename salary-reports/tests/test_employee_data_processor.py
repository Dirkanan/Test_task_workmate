"""
Тесты для модуля чтения данных сотрудников.
"""

import tempfile
import os
import pytest
from utils.employee_data_processor import CSVStaffDataReader

@pytest.fixture
def sample_csv():
    """Фикстура с тестовыми CSV данными"""
    content = "name,department,hours,rate\nJohn,IT,10,100\nJane,HR,20,200\n"
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as temp_file:
        temp_file.write(content)
        temp_file.flush()
        yield temp_file.name
    os.remove(temp_file.name)

def test_csv_reading(sample_csv):
    """Проверка чтения стандартного CSV"""
    reader = CSVStaffDataReader(sample_csv)
    employees = reader.process()
    assert employees == [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
        {"name": "Jane", "department": "HR", "hours": 20, "rate": 200},
    ]

def test_csv_with_hourly_rate_column():
    """Проверка чтения CSV с колонкой hourly_rate"""
    content = "name,department,hours,hourly_rate\nJohn,IT,10,100\n"
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as temp_file:
        temp_file.write(content)
        temp_file.flush()
        reader = CSVStaffDataReader(temp_file.name)
        employees = reader.process()
    os.remove(temp_file.name)
    assert employees == [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
    ]

def test_csv_with_salary_column():
    """Проверка чтения CSV с колонкой salary"""
    content = "name,department,hours,salary\nJohn,IT,10,100\n"
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as temp_file:
        temp_file.write(content)
        temp_file.flush()
        reader = CSVStaffDataReader(temp_file.name)
        employees = reader.process()
    os.remove(temp_file.name)
    assert employees == [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
    ]

def test_nonexistent_file_handling():
    """Проверка обработки отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        reader = CSVStaffDataReader("non_existent_file.csv")
        reader.process()