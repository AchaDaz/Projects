#Программа "Угадай число"
#Компьютер выбирает случайное число от 1 до 100
#Пользователь угадывает
#Компьютер говорит больше или меньше введенного загаданое число
def ask_number(question, low, high, step=1):
    """Просит ввести число из  диапазона"""
    response = None
    while response not in range (low,high,step):
        response = int(input(question))
    return response
import random
def main():
    print("*"*35, "Угадай число", "*"*35)
    print("\nДобро пожаловать!")
    print("\nЯ загадал натуральное число от 1 до 100.")
    print("\nВаша задача - угадать его как можно быстрее.\n")
    print ("\nУ вас 7 попыток. Игра началась.")
    number = random.randint(1,100)
    guess = ask_number("\nВаше предположение: ", 1, 100)
    tries = 1
    while guess != number and tries!=7:
        if guess > number:
            print("Поменьше...")
        else:
            print("Побольше...")
        guess = ask_number("\nВаше предположение: ", 1, 100)
        tries += 1
    if guess == number:
        print(" ")
        print("*"*35, "ПОБЕДА", "*"*35)
        print("\nВам удалось угадать число за ", tries, " попыток\n")
    else:
        print("Получается, не везет...")
main()
input("\n\nНажмите Enter, чтобы выйти...")

