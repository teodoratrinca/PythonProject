
import socket
from tkinter import *



host = '127.0.0.1'
port = 2727
#address = (host,port)

format="utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# GUI class for the INFO
class GUI:
        def __init__(self):
            self.Window = Tk()
            self.Window.withdraw()

            #search window
            self.search = Toplevel()
            self.search.title(" Movie Rating ")
            self.search.config(width = 700, height = 800)

            #create the labels
            self.label1 = Label(self.search,text= "Type your Movie Title:",justify = CENTER,font = "Helvetica 14 bold")
            self.label1.place(relheight=0.16, rely=0.01, relx=0.10)


            self.movieName = Entry(self.search,font="Helvetica 14")
            self.movieName.place(relwidth=0.4,relheight=0.10, rely=0.16, relx=0.10)
            self.movieName.focus()

            # create a Search Button
            self.rating = Button(self.search, text="Search for rating", font="Helvetica 14 bold", command=lambda: self.get1(self.movieName.get()))
            self.rating.place(rely=0.28, relx=0.10)



            self.label2 = Label(self.search, text="Search by actor:", justify=CENTER,font="Helvetica 14 bold")
            self.label2.place(relheight=0.16, rely=0.33, relx=0.10)
            self.actor = Entry(self.search,font="Helvetica 14")
            self.actor.place(relwidth=0.4,relheight=0.10, rely=0.46, relx=0.10)
            self.actor.focus()

            # create a Search Button
            self.rating_actor = Button(self.search,text="Search for rating", font="Helvetica 14 bold",
                                       command=lambda: self.get2(self.actor.get()))
            self.rating_actor.place(rely=0.58, relx=0.10)


            self.label3=Label(self.search, text="Search by a part of movie title:", justify=CENTER,font="Helvetica 14 bold")
            self.label3.place(relheight=0.16, rely=0.63, relx=0.10)
            self.title = Entry(self.search, font="Helvetica 14")
            self.title.place(relwidth=0.4, relheight=0.10, rely=0.76, relx=0.10)
            self.title.focus()
            self.rating_title = Button(self.search, text="Search for rating", font="Helvetica 14 bold",
                                       command=lambda: self.get3(self.title.get()))
            self.rating_title.place(rely=0.88, relx=0.10)
            self.Window.mainloop()


        def get1(self,movieName):
            s.send(('TITLE').encode(format))
            message = movieName
            s.send(message.encode(format))
            self.movieName= s.recv(1024).decode(format)
            self.label4 = Label(self.search, text=self.movieName, font=('helvetica', 10, 'bold'))
            self.label4.place( rely=0.16, relx=0.55)

        def get2(self,actor):
            s.send(('ACTOR').encode(format))
            message = actor
            s.send(message.encode(format))
            self.actor= s.recv(1024).decode(format)
            self.label4 = Label(self.search, text=self.actor, font=('helvetica', 10, 'bold'))
            self.label4.place(rely=0.46, relx=0.55)

        def get3(self,word):
            s.send(('WORD').encode(format))
            message =word
            s.send(message.encode(format))
            self.word= s.recv(1024).decode(format)
            self.label4 = Label(self.search, text=self.word, font=('helvetica', 10, 'bold'))
            self.label4.place(rely=0.76, relx=0.55)


# create a GUI class object
g= GUI()






