"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить
не менее b километров. Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
"""

def days_calc(start_distance, needed_distance):
    day_count = 1
    finish = a
    while finish < b:
        finish *= 1.1
        day_count += 1

    return day_count


a = int(input("Please, enter 1-st day distance: "))
b = int(input("Please, enter needed final distance: "))

print(days_calc(a, b))
