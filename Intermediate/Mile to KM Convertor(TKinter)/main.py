from tkinter import *

window=Tk()
window.title("Mile To Km Convertor")
# window.minsize(width=300,height=120)
window.config(padx=20 ,pady=20)


# Input
input=Entry(width=5)
input.grid(column=1,row=0)

#Label 1
Miles=Label(text="Miles")
Miles.grid(column=2,row=0)

#Label 2
iet=Label(text="is equal to")
iet.grid(column=0,row=1)

#Label 3
output=Label(text="is equal to")
output["text"]= input.get()
output.grid(column=1,row=1)

#Label 4
km=Label(text="KM")
km.grid(column=2,row=1)
def button_clicked():
    mtkm=float(input.get())*1.609344
    output["text"] = round(mtkm)
    #1.609344

#button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=2)


























window.mainloop()
