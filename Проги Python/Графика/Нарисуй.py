from tkinter import*
root = Tk()

canv = Canvas(root, width=500, height=500, bg="lightgray", cursor="pencil")

canv.create_line(200,50,300,50,width=3, fill="blue")
canv.create_line(10,10,10,100,width=2, arrow=LAST)

x=50
y=50
canv.create_rectangle(x,y,x+80,y+50,fill="white", outline="blue")

canv.create_polygon([350,210],[300,250],[300,150], fill="red")

canv.create_oval([20,200],[150,300],fill="gray50")

canv.create_arc([160,230],[230,330],start=0, extent=140, fill="lightgreen")

canv.create_text(20,330, text = "Учимся рисовать",
                 font="times 12", anchor="w", justify=CENTER, fill="red")

canv.pack()

root.mainloop()
