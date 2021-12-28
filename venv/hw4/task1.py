
from sys import argv

script_name, hours_production, rate_per_hour, bonus = argv

print("Имя скрипта: ", script_name)
print("\n Программа расчета ЗП")
print("Отработанные часы: ", hours_production)
print("ЗП в час: ", rate_per_hour)
print("Премия: ", bonus)
print("Итого ЗП: ", (float(hours_production) * float(rate_per_hour)) + float(bonus))
