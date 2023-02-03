"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

dcript_name, hours, salary_in_hour, bonus = argv

salary = float(hours) * float(salary_in_hour) + float(bonus)
print(f'Зарплата сотрудника = {salary:.2f}')