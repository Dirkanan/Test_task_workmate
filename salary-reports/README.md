# 📊 Система генерации отчетов по зарплатам сотрудников

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Возможности

- **Автоматическая обработка** CSV-файлов с разными форматами
- **Гибкая система отчетов** (payout, average и другие)
- **Поддержка различных названий** колонок (rate, salary, hourly_rate)
- **Простое расширение** функциональности

## 📂 Структура проекта

```
salary-reports/
├── data/                   # Тестовые данные
│   ├── data1.csv           # Стандартный формат
│   ├── data2.csv           # Альтернативные названия колонок
│   └── data3.csv           # Разный порядок полей
│
├── tests/                  # Тесты
│   ├── test_employee_data_processor.py
│   ├── test_report.py
│   └── test_report_builder.py
│
├── utils/                  # Основная логика
│   ├── employee_data_processor.py
│   ├── report.py
│   └── report_builder.py
│
├── main.py                 # Точка входа
├── requirements.txt        # Зависимости
└── README.md               # Документация
```

## ⚡ Быстрый старт

### Установка
```bash
git clone https://github.com/yourrepo/salary-reports.git
cd salary-reports
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### Запуск
```bash
python main.py data/data1.csv data/data2.csv data/data3.csv --report payout
```

### Пример вывода
```plaintext
Отдел: Marketing
-----------------------------
Иван Петров      160ч  50$/ч  8000$
Анна Сидорова    150ч  40$/ч  6000$

ИТОГО:           310ч       14000$
```

## 🧪 Тестирование
```bash
# Все тесты
pytest

# С покрытием кода
pytest --cov=utils --cov-report=html

# Конкретный тест
pytest tests/test_report.py -v
```

## 🛠 Расширение системы

### Добавление нового отчета
1. Создайте класс в `report.py`:
```python
class NewReport(BaseReport):
    def build(self, data):
        # Ваша логика
```

2. Зарегистрируйте в `report_builder.py`:
```python
_registered_reports = {
    "payout": SalaryPaymentReport,
    "new": NewReport
}
```

3. Используйте:
```bash
python main.py data.csv --report new
```

## 📌 Поддерживаемые форматы CSV

| Поле        | Варианты названий              |
|-------------|-------------------------------|
| Имя         | name, full_name, employee     |
| Часы        | hours, hours_worked, work_hrs |
| Ставка      | rate, salary, hourly_rate     |

## 📜 Лицензия
MIT License. Copyright (c) 2023 Ваше Имя

---

<div align="center">
  <sub>Создано с ❤️ для автоматизации отчетности</sub>
</div>
```

Ключевые улучшения:
1. Добавлены badges (версия Python, покрытие, лицензия)
2. Улучшена визуальная структура
3. Добавлен пример вывода отчета
4. Четкое разделение блоков
5. Подробное описание расширения системы
6. Добавлена таблица поддерживаемых форматов
7. Современное оформление с иконками
8. Адаптивность для GitHub/GitLab

Файл готов к использованию в репозитории. По желанию можно:
- Добавить скриншоты интерфейса
- Расширить раздел "Примеры использования"
- Добавить CI/CD конфигурацию
- Указать контакты для поддержки