import socket
import webbrowser
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
            self.search.config(width = 760, height = 800)

            #create the labels
            self.label1 = Label(self.search,text= "Type your movie title:",justify = CENTER,font = "Times 16 bold")
            self.label1.place(relheight=0.10, rely=0.06, relx=0.10)


            self.movieName = Entry(self.search,font="Times 14")
            self.movieName.place(relwidth=0.4,relheight=0.10, rely=0.16, relx=0.10)
            self.movieName.focus()
            self.movieName2 = self.movieName
            self.movieName3 = self.movieName

            # create a Search Button
            self.rating = Button(self.search, text="Search for rating", font="Times 14 bold",bg='#C93333',
                                 command=lambda: self.get1(self.movieName.get()))
            self.rating.place(rely=0.28, relx=0.10)

            self.rating1= Button(self.search, text="Search for triler", font="Times 14 bold", bg='#C93333',
                                 command=lambda: self.get4(self.movieName2.get()))
            self.rating1.place(rely=0.28, relx=0.30)

            self.action = Button(self.search, text="See reviews", font="Times 14 bold", bg='#C93333',
                                 command=lambda: self.get5(self.movieName3.get()))
            self.action.place(rely=0.01, relx=0.8)



            self.label2 = Label(self.search, text="Search by actor:", justify=CENTER,font="Times 16 bold")
            self.label2.place(relheight=0.16, rely=0.33, relx=0.10)
            self.actor = Entry(self.search,font="Times 14")
            self.actor.place(relwidth=0.4,relheight=0.10, rely=0.46, relx=0.10)
            self.actor.focus()

            # create a Search Button actor name
            self.rating_actor = Button(self.search,text="Search for rating", font="Times 14 bold",bg='#C93333',
                                       command=lambda: self.get2(self.actor.get()))
            self.rating_actor.place(rely=0.58, relx=0.10)


            self.label3=Label(self.search, text="Search by a part of the movie title:", justify=CENTER,font="Times 16 bold")
            self.label3.place(relheight=0.16, rely=0.63, relx=0.10)
            self.title = Entry(self.search, font="Times 14")
            self.title.place(relwidth=0.4, relheight=0.10, rely=0.76, relx=0.10)
            self.title.focus()
            # create a Search Button
            self.rating_title = Button(self.search, text="Search for rating", font="Times 14 bold",bg='#C93333',
                                       command=lambda: self.get3(self.title.get()))
            self.rating_title.place(rely=0.88, relx=0.10)
            self.search.mainloop()


        def get1(self,movieName):
            s.send(('TITLE').encode(format))
            message = movieName
            s.send(message.encode(format))
            self.movieName = s.recv(1024).decode(format)
            self.label6 = Label(self.search, text=self.movieName, font=('times', 12, 'bold'))
            self.label6.place(rely=0.16, relx=0.55)

        def get2(self, actor):
            s.send(('ACTOR').encode(format))
            message = actor
            s.send(message.encode(format))
            self.actor = s.recv(1024).decode(format)
            self.label4 = Label(self.search, text=self.actor, font=('times', 12, 'bold'))
            self.label4.place(rely=0.46, relx=0.55)

        def get3(self, word):
            s.send(('WORD').encode(format))
            message = word
            s.send(message.encode(format))
            self.word = s.recv(1024).decode(format)
            self.label5 = Label(self.search, text=self.word, font=('times', 12, 'bold'))
            self.label5.place(rely=0.76, relx=0.55)

        def get5(self, name):
            self.name = name
            self.search.destroy()
            self.layout(self.name)

        def layout(self, moviereview):
            self.name = moviereview
            # to show chat window
            self.Window.deiconify()
            self.Window.title(moviereview)
            self.Window.configure(width=760,height=794)
            s.send(('REVIEW').encode(format))
            message = moviereview
            s.send(message.encode(format))  # numele filmului la care dorim review
            self.moviereview = s.recv(4096).decode(format)  # datele despre film
            # data = s.recv(4096).decode(format)
            # print(type(data))
            self.label3 = Label(self.Window, text="Reviews witch match the given title:", justify = CENTER,font=('times', 16, 'bold'))
            self.label3.place(rely=0.05, relx=0.04)
            self.label4 = Label(self.Window, text=self.moviereview, font=('times', 12, 'bold'))
            self.label4.place(rely=0.13, relx=0.04)
            self.label4.config(cursor="arrow")

            self.action = Button(self.Window, text="Close", font="Times 14 bold", bg='#C93333',
                                 command=lambda: self.get6(self.name))
            self.action.place(rely=0.03, relx=0.87)

        def get4(self, movieName):
            new = 1
            s.send(('TRILER').encode(format))
            message = movieName
            s.send(message.encode(format))
            self.movieName = s.recv(1024).decode(format) #url

            def openweb():
                webbrowser.open(self.movieName, new=new)
            openweb()
            self.label4 = Label(self.search, text=self.movieName, font=('times', 12, 'bold'))
            self.label4.place(rely=0.24, relx=0.55)

        def get6(self, name):
            self.Window.destroy()

# create a GUI class object
g= GUI()






