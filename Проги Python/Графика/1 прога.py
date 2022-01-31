from tkinter import*
def hello(event):
    print("Hello, world")

root = Tk()
but1 = Button(root)
but1["text"] = "Привет"
but1.bind("<Button-1>", hello)
but1.pack()
root.mainloop()


    
