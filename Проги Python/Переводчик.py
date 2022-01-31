#Переводчик с гигского на русский
geek = {"404": "Не знать, не владеть информацией",
        "Гуглинг": "Поиск информации в Интернете",
        "Link Rot": "Процесс устаревания гиперссылок на веб-страницах"}
choice = None
while choice != '0':
    print (
    """
    Переводчик с гикского на русский
    0 - Выйти
    1 - Найти толкование термина
    2 - Добавить термин 
    3 - Изменить толкование
    4 - Удалить термин
    """
    )
    choice = input("\nВаш выбор: ")
    if choice == '0':
        print("До скорой встречи!")
    elif choice == '1':
        term = input("\nКакой термин вы хотите перевести:")
        if term in geek:
            definition = geek[term]
            print("\n", term, "означает ", definition)
        else:
            print("Такого слова нет в словаре.")
    elif choice == '2':
        term = input("\nКакой термин хотите добавить?")
        if term not in geek:
            definition = input("\nВведите толкование этого слова:")
            geek[term] = definition
            print ("Данный термин добавлен в словарь.")
        else:
            print("\nТолкование данного слова уже есть.")
    elif choice == '3':
        term = input("\nЗначение какого термина хотите изменить?")
        if term in geek:
            definition = input("\nВпишите ваше толкование: ")
            geek[term]=definition
            print("\nГотово.")
        else:
            print("\nТакого термина нет в словаре.")
    elif choice == '4':
        term = input("Какой термин хотите удалить?")
        if term in geek:
            del geek[term]
            print("\nТермин удален.")
        else:
            print("\nТакого термина и так нет в словаре.")
    else:
        print("В меню нет такого пункта.")
input("\n\nНажмите Enter, чтобы выйти.")
