import qrcode as qr
from tkinter import *
from PIL import Image

def generate():
    img=qr.make(str(e1.get()))
    img.save("z1.png")
    file="z1.png"
    pic=Image.open(file)
    pic.show()


t=Tk()
t.title("QR Code Generator")
t.geometry("800x800")
t.config(bg="skyblue")

l1=Label(t,text="Paste Link here: ",fg="white",bg="black",font=("Arial",20,"bold"))
l1.place(x=10,y=50)

e1=Entry(t,fg="black",font=("Arial",20,"bold"))
e1.place(x=300,y=50,width=350,height=40)

b1=Button(t,text="Generate",fg="black",font=("Arial",20,"bold"),command=generate)
b1.place(x=400,y=100,width=175,height=40)


t.mainloop()