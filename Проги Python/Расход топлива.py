dist = 0 #Расстояние, которое нужно проехать
average_speed = 0 #Средняя скорость авто, км/ч
dist = int(input("Введите расстояние, которое нужно проехать: "))
speed = int(input("Планируемая средняя скорость: "))
time = dist*60/speed
print ("Итак, будет затрачено ", time, " минут")
print ("\n\n")
consum = 0
dist = 0
consume = float(input("Введите расход л./100 км: "))
dist = float(input("Введите расстояние поездки: "))
result = consume*dist/100
print ("Будет затрачено ", result, " литров")
input()
