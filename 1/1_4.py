"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num = int(input("Enter a positive integer: > "))
max_digit = num % 10
num = num // 10
while num > 0:
    if num % 10 > max_digit:
        max_digit = num % 10
    num = num // 10
print(max_digit)

