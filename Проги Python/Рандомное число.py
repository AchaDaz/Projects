#Задаю число в интервале, программа считает с какого раза она угадает рандомно
import random
number = int(input("Введите число для угадывания в диапазоне 1 - 1000: "))
guess = random.randint(1,1000)
tries = 1
while guess != number:
    guess = random.randint(1,1000)
    tries +=1
print("\nЧисло попыток для угадывания: ", tries)
input("\n\nНажмите Enter, чтобы выйти...")
    
