import random
def guess_the_number():
    print("Привет! Добро пожаловать в игру 'Угадай число'!")
    while True:
        secret_number = random.randint(1, 100)
        max_attempts = 10
        attempts = 0
        print("\nЯ загадал число от 1 до 100. У тебя есть 10 попыток, чтобы его найти.")
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nПопытка {attempts + 1}: Введите ваше предположение: "))
            except ValueError:
                print("Ой, кажется, вы ввели не число. Попробуйте еще раз.")
                continue
            attempts += 1

            if guess == secret_number:
                print(f"Поздравляем! Вы успешно угадали число {secret_number} за {attempts} попыток!")
                break
            elif guess < secret_number:
                print("Ваше число меньше загаданного.")
            else:
                print("Ваше число больше загаданного.")
        else:
            print(f"\nК сожалению, попытки закончились. Загаданное число было: {secret_number}.")
        play_again = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again not in ('да', 'д', 'yes', 'y'):
            print("Спасибо за игру! До свидания!")
            break
if __name__ == "__main__":
    guess_the_number()
