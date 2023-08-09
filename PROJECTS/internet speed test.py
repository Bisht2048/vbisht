import speedtest
from tkinter import *

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    # down=round(sp.download)
    down=str(round(sp.download()/(10**6),2))+" Mbps"
    up=str(round(sp.upload()/10**6,2))+ " Mbps"
    d1.config(text=down)
    u1.config(text=up)

    # print(down)
    # print(up)

# speedcheck()

t=Tk()
t.title("Internet Speed Test")
t.geometry("750x500")
t.config(bg="Black")

label1=Label(t,fg="Red",bg="White",text="Download Speed ",font=("Time New Roman",20,"bold"),relief=RAISED)
label1.place(x=100,y=50,height=50,width=250)

label2=Label(t,fg="Red",bg="White",text="Upload Speed ",font=("Time New Roman",20,"bold"),relief=RAISED)
label2.place(x=100,y=150,height=50,width=250)

d1=Label(t,fg="black",bg="green",text="00",font=("Calibiri",20,"bold"),relief=RAISED)
d1.place(x=400,y=50,height=50,width=250)

u1=Label(t,fg="black",bg="orange",text="00",font=("Calibiri",20,"bold"),relief=RAISED)
u1.place(x=400,y=150,height=50,width=250)

b1=Button(t,text="Check Speed",font=("Time New Roman",30,"bold"),relief=FLAT,bg="red",command=speedcheck)
b1.place(x=250,y=250)
t.mainloop()