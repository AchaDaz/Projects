#Компьютер угадывает число
#Реализуем при помощи середины отрезков
#Компьютер будет предлагать серидины, пока не угадает
print("Программа по угадыванию числа готова!")
start = int(input("\nВведите начало промежутка угадывания: "))
end = int(input("\nВведите конец промежутка угадывания: "))
print("\nЕсли надо побольше, то +, если поменьше, то -. А если угадано, то 0")
input("\nЕсли загадали число, нажмите Enter...")
response = " "
guess = 0
tries = 0
import math
while response != "0":
    tries += 1
    guess = math.ceil((start+end)/2)
    print(guess)
    response = input("\nПобольше или поменьше? ")
    if response == "+":
        start = guess
    elif response == "-":
        end = guess
    elif response == "0":
        break
    if response != 0 and (guess == start +1):
        response = "0"
        guess = start
    elif response !=0 and (guess == end -1):
        response = "0"
        guess = end    
print("\n\nИтак, Вы загадали число ", guess)
print("\nИ оно было угадано с ", tries, " попытки.")
input("\n\nНажмите Enter, чтобы выйти...")
