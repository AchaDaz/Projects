#Программа по выводу 8 слов в случайном порядке
import random
words = ["Морковка", "Коровка", "Шорох", "Кекс"]
while words:
   print(words.pop(random.randint(0, len(words)-1)))
input("\nНажмите Enter, чтобы выйти")
