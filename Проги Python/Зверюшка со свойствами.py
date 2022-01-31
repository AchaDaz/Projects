class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger = 0, boredom = 0):
       self.name = name
       self.hunger = hunger
       self.boredom = boredom
    def __pass_time(self):
        self.hunger +=3
        self.boredom +=3
    def __str__(self):
        ans = "Имя: " + str(self.name)
        ans += "\nГолод: " + str(self.hunger)
        ans += "\nУныние: " + str(self.boredom)
        return ans
   
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
        while food <1 or food >5:
            food = int(input("Сколько еды хотите скормить?"))
        print("От души!")
        self.hunger -=food
        if self.hunger <0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = 0
        while fun <1 or fun >5:
           fun = int(input("Сколько часов хотите поиграть?"))
        print("Вот это игра!")
        self.boredom -= fun
        if self.boredom <0:
            self.boredom = 0
        self.__pass_time

def main():
    crit_name = input("Как назовем? ")
    crit = Critter(crit_name)
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
input("\n\nНажмите Enter, чтобы выйти.")



