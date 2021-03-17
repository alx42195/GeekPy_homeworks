"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.
"""

def profitability(revenue, expenditures, employees):
    profit = (revenue - expenditures) / revenue
    per_capita = profit / employees

    return f"Profitability is {profit}\nProfitability per person is {per_capita}"

revenue = float(input("Enter the revenue, please > "))
expenses = float(input("Enter the expenses, please > "))

if revenue > expenses:
    print("The company is profitable")
    employees_num = int(input("How many employees do you have? > "))
    print(profitability(revenue, expenses, employees_num))
else:
    print("The company is unprofitable")



