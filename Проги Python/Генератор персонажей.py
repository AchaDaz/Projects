#Генератор персонажей
#Создаем массив, в котором будет 4 хараткеристики
parameter = {"Сила": 0,
             "Здоровье": 0,
             "Мудрость": 0,
             "Ловкость": 0}
pool = 100 #Задаем пул характеристик для распределения
print("Программа по генерацию персонажей.")
choice = None
while choice != '0':
    print(
        """
        0 - Выйти из программы
        1 - Добавить характеристики из пула
        2 - Убрать характеристики в пул
        """
        )
    choice = input("\nВведите ваш выбор: ")
    if choice == '0':
        print("\nК концу программы ваш персонаж выглядит так")
        print(parameter)
    elif choice == '1':
        print("\nХарактеристик для распределения:", pool)
        print("\nТекущие характеристики ", parameter)
        print(
            """
            1 - Добавить Силы
            2 - Добавить Здоровья
            3 - Добавить Мудрости
            4 - Добавить Ловкости
            """
            )
        choice = input('\nВаш выбор? ')
        if choice == '1':
            num = int(input("Сколько силы хотите добавить:"))
            if num > pool:
                print("У вас столько нет!")
            else:
                parameter["Сила"] += num 
                pool -= num
                print("\nДобавлено!")
        elif choice == '2':
            num = int(input("Сколько здоровья хотите добавить:"))
            if num > pool:
                print("У вас столько нет!")
            else:
                parameter["Здоровье"] += num 
                pool -= num
                print("\nДобавлено!")
        elif choice == '3':
            num = int(input("Сколько мудрости хотите добавить:"))
            if num > pool:
                print("У вас столько нет!")
            else:
                parameter["Мудрость"] += num 
                pool -= num
                print("\nДобавлено!")
        elif choice == '4':
            num = int(input("Сколько ловкости хотите добавить:"))
            if num > pool:
                print("У вас столько нет!")
            else:
                parameter["Ловкость"] += num 
                pool -= num
                print("\nДобавлено!")
        else:
            print("\nТакого параметра нет в меню!")
    elif choice == '2':
        print("\nТекущие характеристики ", parameter)
        print("\nХарактеристик в пуле:", pool)
        print(
            """
            1 - Уменьшить Силу
            2 - Уменьшить Здоровье
            3 - Уменьшить Мудрость
            4 - Уменьшить Ловкость
            """
            )
        choice = input('\nВаш выбор? ')
        if choice == '1':
            num = int(input("Сколько силы хотите убрать? "))
            if (parameter["Сила"]-num)<0:
                print("У вас столько нет силы!")
            else:
                pool += num
                parameter["Сила"] -=num
                print("Убавлено!")
        elif choice == '2':
            num = int(input("Сколько здоровья хотите убрать? "))
            if (parameter["Здоровье"]-num)<0:
                print("У вас столько нет здоровья!")
            else:
                pool += num
                parameter["Здоровье"] -=num
                print("Убавлено!")
        elif choice == '3':
            num = int(input("Сколько мудрости хотите убрать? "))
            if (parameter["Мудрость"]-num)<0:
                print("У вас столько нет мудрости!")
            else:
                pool += num
                parameter["Мудрость"] -=num
                print("Убавлено!")
        elif choice == '4':
            num = int(input("Сколько ловкости хотите убрать? "))
            if (parameter["Ловкость"]-num)<0:
                print("У вас столько нет ловкости!")
            else:
                pool += num
                parameter["Ловкость"] -=num
                print("Убавлено!")
input("\n\nНажмите Enter, чтоьы выйти.")
