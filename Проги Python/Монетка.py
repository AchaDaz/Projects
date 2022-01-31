#Монетку подрбасывают 100 раз, считаем орлы и решки
import random
tries = 0
result = 0
orel = 0
reshka = 0
print("Программа по подбрасыванию монетки приветствует Вас!")
print("\nМы подбросим за вас 100 раз монетку и скажем число орлов и решек.")
input("\n\nНажмите Enter, чтобы начать подбрасывание...")
while tries < 100:
    tries +=1
    result = random.randint(1,2)
    if result == 1:
        orel += 1
    else:
        reshka += 1
print("\n\nЧисло орлов: ", orel)
print("\nЧисло решек: ", reshka)
input("\nНажмите Enter, чтобы выйти...")
