"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = input("Enter the number: > ")

print(f"{int(n)+int(n+n)+int(n+n+n)}")