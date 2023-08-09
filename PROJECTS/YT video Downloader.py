from pytube import YouTube
from tkinter import *

link="https://www.youtube.com/watch?v=OKuiyX5k6zg&ab_channel=WsCubeTech"
youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

videos= youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter: "))
videos[strm].download()

print('successful')
#
# t=Tk()
# t.title("Youtube Videos Downloader")
# t.geometry("750x750")
# t.config(bg="white")
#
#
#
# label=Label(t,fg="Red",text="Paste Your Link Here:",bg="Silver",font=("Arial",15,"bold"))
# label.place(x=0,y=10)
# e=Entry(t,fg="Black",font=("New Times Roman",15))
# e.place(x=250,y=10)
#
#
# def hi():
#     h=Label(t,text="Successful",font=("Arialbold",14,"bold"))
#     h.place(x=280,y=70)
#     a = str(e.get())
#
#     youtube_1 = YouTube(a)
#     videos= youtube_1.streams.all()
#     vid=list(enumerate(videos))
#     for i in vid:
#         print(i)
#
#     strm = int(input("Enter: "))
#     videos[strm].download()
#
#     print('successful')
#     label5 = Label(t, text="The file has been Downloaded.", font=('Arial', 15, 'bold'))
#     label5.place(x=200, y=300)
#
# b = Button(t, text="Start Download",bg="Red",font=("Arialbold",15,"bold"), command=hi)
# b.place(x=250,y=150)
#
#
# t.mainloop()