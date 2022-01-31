#Та же программа угадай число
#Но с графическим интерфейсом
from tkinter import*
class Application(Frame):
    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.tries = 0
        self.NUM = random.randint(1,100)
    def create_widgets(self):
        Label(self,
              text = "Вас приветствует программа 'Угадай число!'"
              ).grid(row=0, column=0, columnspan = 2, sticky = W)
        Label(self,
              text = "Программа загадала число от 1 до 100"
              ).grid(row=1, column=0, columnspan = 2, sticky = W)
        Label(self,
              text = "Ваша задача его угадать."
              ).grid(row=2, column=0, columnspan = 2, sticky = W)
        Label(self,
              text = "Ваше предположение: "
              ).grid(row=3, column=0, columnspan = 1, sticky = W)
        self.response = Entry(self)
        self.response.grid(row=3, column = 1, sticky = W)
        Button(self,
               text = "Проверить значение",
               command = self.check_num
               ).grid(row=4, column=0, columnspan = 2, sticky = W)
        self.text = Text(self, width = 50, height = 3, wrap = WORD)
        self.text.grid(row=5, column=0, columnspan = 4)
        Button(self,
               text = "Получить новое значение",
               command = self.refresh
               ).grid(row=8, column=0, columnspan = 3, sticky = S)

    def check_num(self):
        num = self.response.get()
        result = ""
        if self.tries <= 10:
            if int(num) == self.NUM:
                result = "Поздравляю! Вы победили!"
            if int(num) > self.NUM:
                result = "Выберете число чуть поменьше..."
            if int(num) < self.NUM:
                result = "Выберете число чуть побольше..."
        else:
            result = "Попытки закончились! Вы проиграли!"
        self.text.delete(0.0, END)
        self.text.insert(0.0, result)
        self.tries += 1
        
    def refresh(self):
        self.NUM = random.randint(1,100)
        self.tries = 0
        self.text.delete(0.0, END)
        self.response.delete(0, END)

import random
root = Tk()
root.title("Угадай число")
app = Application(root)
root.mainloop()
