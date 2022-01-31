#Анаграммы (Word Jumble)
#Компьютер переставляет в слове буквы
#Цель игрока - угадать слово
import random
WORDS = ("пукич", "хартстоун", "эксперимент", "курва", "курсив", "кетчуп",
         "эльдорадо", "бутылка", "танцы", "айфон", "адаптер")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print("*"*35, "Анаграммы", "*"*35)
print("\nЗадача: переставить буквы, чтобы получилось осмысленное слово")
print("\nДля выхода нажмите Enter, не ввода своей версии")
print("Вот анаграмма: ", jumble)
response = input("\nЕсли хотите подсказку, нажмите +.")
if response == "+":
    print("\nПодсказка: слово начинается на ", correct[0], " и заканчивается на ", correct[-1])
guess = input("\nПопробуйте отгадать исходное слово: ")
total = 100
while guess != correct and guess != "" and total > 0:
    print ("\nК сожалению, вы неправы.")
    guess = input("\nПопробуйте отгадать исходное слово: ")
    if response == "+":
        total -= 17
    else:
        total -= 10
if guess == correct:
    print("Да, именно так! Победа!")
    print ("Ваше количество очков :", total)
if total < 0:
    print ("Вы проиграли, стараться лучше надо...")
print ("Спасибо за игру.")
input ("\n\nНажмите Enter, чтобы выйти...")
