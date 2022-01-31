from tkinter import*

root = Tk()

var0 = StringVar()
var1 = StringVar()
var2 = StringVar()

ch0 = Checkbutton(root, text="Windows", variable=var0,
                  onvalue="Windows", offvalue="-")
ch1 = Checkbutton(root, text="Linux", variable=var1,
                  onvalue="Linux", offvalue="-")
ch2 = Checkbutton(root, text="macOS", variable=var2,
                  onvalue="macOS", offvalue="-")

lis = Listbox(root, height=3)

def result(event):
    v0 = var0.get()
    v1 = var1.get()
    v2 = var2.get()
    l = [v0, v1, v2]
    lis.delete(0,20)
    for v in l:
        lis.insert(END, v)

but = Button(root, text = "Получить значения")
but.bind("<Button-1>", result)

ch0.deselect()
ch1.deselect()
ch2.deselect()

ch0.pack()
ch1.pack()
ch2.pack()
but.pack()
lis.pack()

root.mainloop()
