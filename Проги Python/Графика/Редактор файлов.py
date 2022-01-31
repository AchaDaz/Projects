from tkinter import*
from tkinter.filedialog import*
import fileinput

def _open():
    op = askopenfilename()
    print(op)
    f = open(op, "r", encoding='utf-8')
    content = f.read()
    txt.delete(1.0, END)
    txt.insert(END, content)

def _save():
    sa = asksaveasfilename()
    content = txt.get(1.0, END)
    f = open(sa, "w", encoding='utf-8')
    f.write(content)
    f.close()

root = Tk()

txt = Text(root, width=40, height=15, font="Courier 10")
txt.pack()

m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label = "Файл", menu=fm)
fm.add_command(label = "Открыть...", command=_open)
fm.add_command(label = "Сохранить как...", command=_save)



root.mainloop()
