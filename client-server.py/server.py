import pickle
import pymongo
import socket
from pprint import PrettyPrinter
import tkinter as tk
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MovieDB"]
mycol = mydb["movies"]
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 700, height = 600,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Movies Ratings')
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=label1)

label2 = tk.Label(root, text='Type your Movie Title:')
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 100, window=label2)

label3 = tk.Label(root, text='Search by actor:')
label3.config(font=('helvetica', 10))
canvas1.create_window(300, 260, window=label3)

label4 = tk.Label(root, text='Search by a part of movie title:')
label4.config(font=('helvetica', 10))
canvas1.create_window(300, 400, window=label4)

entry1 = tk.Entry (root)
canvas1.create_window(300, 140, window=entry1)
entry2 = tk.Entry (root)
canvas1.create_window(300, 290, window=entry2)
entry3 = tk.Entry (root)
canvas1.create_window(300, 430, window=entry3)

def ratings(title):
  myquery={'Title':title}
  mydoc = mycol.find(myquery)
  for x in mydoc:
     return (x['imdbRating'])
  return ("Nu s a gasit filmul")
#cautare dupa titlu

def cautare_dupa_cuvant(word):
  gasit = 0
  allmovie = ""
  for x in mycol.find():
      titles = {"title": x['Title'], "imdbRating": x['imdbRating']}
      words = titles['title'].split(' ')
      if word in words:
          print(word)
          gasit = 1
          allmovie = allmovie + str(titles['title'])
          allmovie = allmovie + str(" with rating: ")
          allmovie = allmovie + str(titles['imdbRating'])
          allmovie = allmovie + str(" \n")
  if (gasit == 0):
      return ("Nu s-a putu gasi film")
  else:
      return (allmovie)


#print(cautare_dupa_titlu("Titanic"))


def cautare_dupa_actor(actor):
  gasit=0
  allmovie=""
  for x in mycol.find():
    actors ={ "title": x['Title'],"actors": x['Actors'],"imdbRating": x['imdbRating']}
    words = actors['actors'].split(', ')
    print(words)
    if actor in words:
        gasit=1
        allmovie= allmovie+str(actors['title'])
        allmovie = allmovie + str(" with rating: ")
        allmovie= allmovie+str( actors['imdbRating'])
        allmovie= allmovie +str(" \n")
  if (gasit == 0):
    return ("Nu s-a putu gasi film")
  else:
      return(allmovie)

#print(cautare_dupa_actor('Kate Winslet'))

def getRating():
    x1 = entry1.get()

    label3 = tk.Label(root, text='The Rating of the movie is:', font=('helvetica', 10))
    canvas1.create_window(300, 210, window=label3)

    label4 = tk.Label(root, text=ratings(x1), font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 230, window=label4)
def getRatingByActor():
    x1 = entry2.get()

    label3 = tk.Label(root, text='The rating of movies in which the actor plays:', font=('helvetica', 10))
    canvas1.create_window(300, 320, window=label3)

    label4 = tk.Label(root, text=cautare_dupa_actor(x1), font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 370, window=label4)
def getRatingByTitle():
    x1 = entry3.get()

    label3 = tk.Label(root, text='The rating of movies containing the name:', font=('helvetica', 10))
    canvas1.create_window(300, 470, window=label3)

    label4 = tk.Label(root, text=cautare_dupa_cuvant(x1), font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 510, window=label4)


button1 = tk.Button(text='Get the Rating', command=getRating, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 180, window=button1)
button2 = tk.Button(text='Get the Rating', command=getRatingByActor, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(450, 290, window=button2)
button4 = tk.Button(text='Get the Rating', command=getRatingByTitle, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(450, 430, window=button4)

root.mainloop()


# pp = PrettyPrinter()
#
# host = '127.0.0.1'
# port = 2727
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))
# s.listen(10)
#


#
# while True:
#     clientsocket, addr = s.accept()
#     print(f"Conexiunea cu {addr} a fost stabilita cu succes!")
#     clientsocket.send(bytes("Bine ati venit", "utf-8"))
#     msg = clientsocket.recv(4096)
#     title = msg.decode("utf-8")
#     print("Clientul doreste ratingul filmului: ", title)
#     data = ratings(title)
#     msg = pickle.dumps(data)
#     print(msg)
#     clientsocket.send(msg)
#     #print(type(data))
#     #print(data)
#
#





