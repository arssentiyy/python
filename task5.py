# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
dx = int(input("Введите сумму дохода "))
r = int(input("Введите сумму расхода "))

if dx > r and dx != 0:
    print("Отработано с прибылью")
    print("Рентабельность= " + str((dx - r) / dx))
    x = int(input("Введите кол-во сотрудников компании "))
    print("Прибыль на 1го сотрудника= " + str((dx - r) / x))
elif dx <= r:
    print("Отработано с убытком ")




