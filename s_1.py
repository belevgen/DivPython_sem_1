# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

REFORM = 1582
BIG_LEAP_YEAR = 400
LARGE_NON_LEAP_YEAR = 100
SMALL_LEAP_YEAR = 4
MULTIPLE = 0
year = int(input("Введите год: "))

if year < REFORM:
    result = "Григорианский календар не введен"
elif year % BIG_LEAP_YEAR == MULTIPLE:
    result = f"{year} - Високосный год"
elif year % LARGE_NON_LEAP_YEAR == MULTIPLE:
    result = f"{year} - Не високосный год"
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    result = f"{year} - Високосный год"
else:
    result = f"{year} - Не високосный год"

print(result)
