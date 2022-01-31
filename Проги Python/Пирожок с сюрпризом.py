#Через рандом выбираем число и через if выводим
import random
import winsound
number = random.randint(1,5)
print("Программа 'Пирожок с сюрпризом'")
input("\nНажмите Enter для продолжения...")
print("\n\nВы берете пирожок и он оказывается...")
winsound.Beep(2500, 2000)
if number == 1:
    print("\n\nС вишней!!!")
elif number == 2:
    print("\n\nC картошкой!!!")
elif number == 3:
    print("\n\nС мясом!!!")
elif number == 4:
    print("\n\nС яблоком!!!")
elif number == 5:
    print("\n\nС маком!!!")
print("\n\nПриятного аппетита!")
input("\n\nНажмите Enter, чтобы выйти...")

