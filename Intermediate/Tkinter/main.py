from tkinter import *

window=Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100 ,pady=200)

#Label
my_label=Label(text="I am a Label",font=("Arial",24,"bold"))
# my_label.pack(side="bottom",expand=True)
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
# my_label["text"]= "New Text"        Method 1
# my_label.config(text="New Text")    Method 2
my_label.config(padx=50, pady=70)
#Button
def button_clicked():
    my_label["text"]= input.get()


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)



button2 = Button(text="Click Me Plz", command=button_clicked)
# button.pack()
button2.grid(column=2,row=0)
#Entry
input=Entry(width=10)
# input.pack()
input.grid(column=3,row=2)
print(input.get())





























window.mainloop()