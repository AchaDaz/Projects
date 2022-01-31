import pickle
mark = 0
print ("*"*37, "Тесты", "*"*36)
try:
    datafile = open("test.dat", "rb")
except:
    print ("Ошибка при загрузке вопросов!")
else:
    questions = pickle.load(datafile)
    answers = pickle.load(datafile)
    datafile.close()
    n = len(answers)
    for i in range(0, n):
        print(questions[i])
        a = int(input("Ваш ответ: "))
        if a == answers[i]:
            mark += 1
            print ("Верно!")
        else:
            print ("Неверно!")
    print("\nВы правильно ответили на ", mark, " вопросов из", n)
    
