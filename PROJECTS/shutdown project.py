import os
from tkinter import *

def ShutDown():
    os.system("shutdown /s /t 1")

def Restart():
    os.system("restart /r /t 1")

def Sleep():
          os.system("shutdown -l")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Black")

b1= Button(st,text="Restart",font=("Arial",30,"bold"),relief=RAISED,command=Restart)
b1.place(x=150,y=200,height=40,width=200)

b2= Button(st,text="ShutDown",font=("Arial",30,"bold"),relief=RAISED,command=ShutDown)
b2.place(x=150,y=400,height=40,width=200)

b3= Button(st,text="Sleep",font=("Arial",30,"bold"),relief=RAISED,command=Sleep)
b3.place(x=150,y=20,height=40,width=200)





st.mainloop()

