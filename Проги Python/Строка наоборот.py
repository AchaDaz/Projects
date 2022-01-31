#Программа разворачивает наоборот пользовательскую строку
line = input("Введите строку: ")
for i in range(-1, -len(line), -1):
    print(line[i], end="")
input("n\nНажмите Enter, чтобы выйти...")
