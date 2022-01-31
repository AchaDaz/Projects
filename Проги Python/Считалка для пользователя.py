#Считалка для пользователя
#Задаем начало, конец, шаг, программа выводит цифры на экран
print ("Программа 'Счетчик'")
start = int(input("\nВведите начало отсчета: "))
finish = int(input("\nВведите конец отсчета: "))
step = int((input("\nВведите шаг: ")))
for i in range (start, finish, step):
    print(i, end= " ")
input("\nНажмите Enter, чтобы выйти...")
