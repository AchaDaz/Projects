s1 = "Lorem ipsum dolor sit amet, consecteture adipiscing elit. "
s2 = "Proin porta, liberto sit amet porttitor tempor, sapien diam vulputate"
s3 = "liberto, quis porttitor nulla leo auctor felis."
print (s1+s2+s3)
print ("\n\n")

print ("*"*80)
print ("\n")
test = "Здарова епта"
print (test.upper()) #Выведется все в верхнем регистре
print (test) #Показываем, что исходная строка не изменилась
test = test.upper()
print (test) #Исходная строка в новом регистре
print (test.lower())
test = test.swapcase() #Поменяли регистр каждой буквы на противоположный
print (test.capitalize()+"\n")
test = "У Григория есть 100 енотов"
print(test.replace("100 енотов", "огромное очко"))
input()
