#Счет, пожалуйста!
#Программа с выбором элементов меню и дальнейшим выводом цены
from tkinter import*
class Application(Frame):
    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Добро пожаловать в лучший ресторан!",
              ).grid(row=0, column=0, columnspan=5, sticky = S)
        Label(self,
              text = "Собирите свой обед из ниже перечисленных блюд."
              ).grid(row=1, column=0, columnspan=5, sticky = S)
        Label(self,
              text = "Первое:"
              ).grid(row=2, column=0, sticky=W)
        Label(self,
              text = "Второе:"
              ).grid(row=3, column=0, sticky=W)
        Label(self,
              text = "Напиток:"
              ).grid(row=4, column=0, sticky=W)
        Label(self,
              text = "Десерт:"
              ).grid(row=5, column=0, sticky=W)
        self.soup = StringVar()
        self.soup.set(None)
        self.meat = StringVar()
        self.meat.set(None)
        self.drink = StringVar()
        self.drink.set(None)
        self.cake = StringVar()
        self.cake.set(None)
        soups = ["щи", "борщ", "грибной суп"]
        meats = ["паста", "котлеты", "отбивная"]
        drinks = ["чай", "кофе", "сок"]
        cakes = ["кекс", "блины", "суфле"]
        column = 1
        for soup in soups:
            Radiobutton(self,
                        text = soup,
                        variable = self.soup,
                        value = soup
                        ).grid(row =2, column = column, sticky = W)
            column += 1

        column = 1
        for meat in meats:
            Radiobutton(self,
                        text = meat,
                        variable = self.meat,
                        value = meat
                        ).grid(row =3, column = column, sticky = W)
            column += 1

        column = 1
        for drink in drinks:
            Radiobutton(self,
                        text = drink,
                        variable = self.drink,
                        value = drink
                        ).grid(row =4, column = column, sticky = W)
            column += 1

        column = 1
        for cake in cakes:
            Radiobutton(self,
                        text = cake,
                        variable = self.cake,
                        value = cake
                        ).grid(row =5, column = column, sticky = W)
            column += 1
        
        self.text = Text(self, width = 100, height = 5, wrap = WORD)
        self.text.grid(row=7, column =0, columnspan = 4)
        Button(self,
               text = "Потвердить",
               command = self.account
               ).grid(row = 6, column = 0, columnspan = 5, sticky = S)
    def account(self):
        soup = self.soup.get()
        meat = self.meat.get()
        drink = self.drink.get()
        cake = self.cake.get()
        money = 0
        if soup == "щи":
            money += 100
        elif soup == "борщ":
            money += 120
        elif soup == "грибной суп":
            money += 110
        if meat == "паста":
            money += 250
        elif meat == "котлеты":
            money += 220
        elif meat == "отбивная":
            money += 230
        if drink == "чай":
            money += 80
        elif drink == "кофе":
            money += 120
        elif drink == "сок":
            money += 90
        if cake == "кекс":
            money += 100
        elif cake == "блины":
            money += 120
        elif cake == "суфле":
            money += 110
        response = "Итак, ваш выбор: "
        response += soup + ", "
        response += meat + ", "
        response += drink + ", "
        response += cake + ". "
        response += "Итого к оплате: " + str(money) + "."
        self.text.delete(0.0, END)
        self.text.insert(0.0, response)

root = Tk()
root.title("Симулятор ресторана")
app = Application(root)
root.mainloop()
