import phonenumbers
from phonenumbers import carrier
from tkinter import *

def search():
    number=e1.get()
    number="+91"+number
    phone=phonenumbers.parse(number)
    car=carrier.name_for_number(phone,"en")
    print(phone)
    print(car)
    p2=f"This Number is of {car}."
    l2.config(text=p2)


t=Tk()
t.title("Phone Number Details")
t.geometry("500x500")

l1=Label(text="Enter Phone Number ",font=15)
l1.place(x=10,y=150)

e1=Entry(font="bold")
e1.place(x=225,y=150,height=25,width=200)

b1=Button(text="Search Now!",font="Arialbold",command=search)
b1.place(x=240,y=205,height=50,width=150)

l2=Label(font=15)
l2.place(x=100,y=400)

t.mainloop()



