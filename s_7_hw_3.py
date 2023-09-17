# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

num_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)                 # Генерируем случайное число, которое нужно угадать

print("Добро пожаловать в игру 'Угадай число'!")
print(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT} за {MAX_ATTEMPTS} попыток.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"Попытка {attempt}. Введите вашу догадку: "))

    if guess < num_to_guess:
        print("Число больше.")
    elif guess > num_to_guess:
        print("Число меньше.")
    else:
        print(f"Поздравляем! Вы угадали число {num_to_guess} за {attempt} попыток.")
        break
else:
    print(f"Игра окончена. Вы не угадали число. Загаданное число было: {num_to_guess}")
