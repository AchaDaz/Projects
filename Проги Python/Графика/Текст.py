from tkinter import*

root = Tk()

tx = Text(font=('times', 12), width=50, height=15, wrap=WORD)
tx.pack(expand=YES, fill=BOTH)

tx.insert(1.0, 'Строка 1\n\
Строка 2\n\n\
Строка 3')

tx.tag_add('title', '1.0', '1.end')
tx.tag_add('special', '6.0', '8.end')
tx.tag_add('special', '3.0', '3.11')

tx.tag_config('title', foreground='red', font=('Arial', 14, 'underline'), justify=CENTER)
tx.tag_config('special', background='grey85', font=('times', 10, 'bold'))

def erase():
    tx.delete('1.0', END)

bt = Button(tx, text='Очистить', command = erase)
tx.window_create(END, window=bt)


root.mainloop()
