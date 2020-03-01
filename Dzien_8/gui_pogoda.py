import tkinter
from request_przyklady import link_miasto, link_lokalizacja, pogoda

def pobierz_dane():
    pogoda(miasto_entry)


root = tkinter.Tk()
label_miasto = tkinter.Label(master=root, text="Wprowadź miasto")
label_miasto.pack()
miasto_entry = tkinter.Entry(master=root)
miasto_entry.pack()
submit = tkinter.Button(master=root, text = "Sprawdź pogodę", command(pobierz_dane()))
submit.pack()

root.mainloop()
