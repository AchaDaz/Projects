#Программа Зооферма
#Та же зверюшка, но только ферма
import random
class Critter(object):
    """Зооферма"""
    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger +=1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <=10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать, что хорошо"
        else:
            m = "при смерти"
        return m

    def talk(self):
        print("Меня зовут", self.name, " и сейчас я чувствую себя ", self.mood)
        self.__pass_time()

    def eat(self):
        food = 0
        while food <= 1 or food >= 10:
            food = int(input("Сколько еды получит "+self.name+":"))
        self.hunger -=food
        if self.hunger <0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = 0
        while fun <1 or fun >10:
           fun = int(input("Сколько часов игры получит "+self.name +":"))
        print("Вот это игра!")
        self.boredom -= fun
        if self.boredom <0:
            self.boredom = 0
        self.__pass_time

    def __str__(self):
        ans = "Имя: " + str(self.name)
        ans += "\nГолод: " + str(self.hunger)
        ans += "\nУныние: " + str(self.boredom)
        return ans
         

def main():
    farm = []
    crit_num = input("Сколько зверюшек хотите завести: ")
    for crit in range(int(crit_num)):
        crit_name = input("\nКак назовете зверюшку? ")
        crit = Critter(crit_name, hunger = random.randint(1,16), boredom = random.randint(1,16))
        farm.append(crit)

    choice = None
    while choice != "0":
        print \
        ("""
        Моя зверюшка
        0 - Выйти в окно
        1 - Спросить как дела
        2 - Дать покушать
        3 - Поиграть
        """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print ("До свидания!")
        elif choice == "1":
            for crit in farm:
                crit.talk()
        elif choice == "2":
            for crit in farm:
                crit.eat()
        elif choice == "3":
            for crit in farm:
                crit.play()
        elif choice == "4":
            for crit in farm:
                print(crit)
                print()
        else:
            print("Извините, но такого пункта нет в меню.")
        
main()
input("\n\nНажмите Enter, чтобы выйти")
    

    
        
