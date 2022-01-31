try:
    a = int(input("Введите целое число а: "))
    b = int(input("Введите целое число b: "))
    print("a/b = ", a/b)
except ValueError:
    print("Необходимо ввести число!")
except ZeroDivisionError as e:
    print("На ноль делить нельзя!")
    print("Интерпретатор ругается:")
    print(e)
