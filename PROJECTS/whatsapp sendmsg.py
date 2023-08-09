import pywhatkit as whatsapp
from tkinter import *


# def whats(n,msg):
#     whatsapp.sendwhatmsg_instantly('+91','n','msg',10)


# whatsapp.sendwhatmsg('+919311784030','Hi i am python',17,13)
# whatsapp.sendwhatmsg_instantly('+919311784030','Hi i am python ',10)
t=Tk()
t.title("Whatsapp Automation")
t.geometry("786x786")
# t.config(bg="Blue")

# frame= Frame(t,borderwidth=6,bg="Grey",relief=SUNKEN)
# frame.pack(side=RIGHT,anchor="s")
#
# b1=Button(frame,text="Send Message",fg="red",font=("Arial",15,"bold"))
# b1.pack(side=LEFT,padx=0,pady=0)
# b1.place(x=10)

lable1=Label(t,text="Enter Number Here: ",fg="Black",font=("Arial",20,"bold"))
lable1.grid(row=0,column=1,padx=0,pady=50)

textbox1=Entry(t,fg="Black",font=("New Times Roman",25,"bold"))
textbox1.grid(row=0,column=2)

label2=Label(t,text="Enter your Message Here: ",fg="black",font=("Arial",20,"bold"))
label2.grid(row=1,column=1)

data2=StringVar()
print(data2)

textbox2=Entry(t,fg="Black",font=("New Times Roman",25,))
textbox2.grid(row=1,column=2)

def pr():
    a = str(textbox1.get())
    msg = str(textbox2.get())
    print(a)
    print(msg)
    whatsapp.sendwhatmsg_instantly(f"+91{a}",msg)

b1=Button(t,text="Send Now",fg="red",font=("Arial",25,"bold"),command=pr)
b1.place(x=400,y=200)


t.mainloop()