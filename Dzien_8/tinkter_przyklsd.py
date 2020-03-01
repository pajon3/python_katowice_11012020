import tkinter

def sumuj():
    a = a_entry.get()
    b = b_entry.get()



root= tkinter.Tk()
label_a  = tkinter.Label(master=root, text = "a")
label_a.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
label_b  = tkinter.Label(master=root, text = "b")
label_b.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

submit = tkinter.Button(master=root, tekst = "SUMUJ", command = sumuj)



root.mainloop()