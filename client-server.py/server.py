import pickle
import pymongo
import socket
from pprint import PrettyPrinter

pp = PrettyPrinter()

host = '127.0.0.1'
port = 2727

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MovieDB"]
mycol = mydb["movies"]


def ratings(title):
  myquery={'Title':title}
  mydoc = mycol.find(myquery)
  for x in mydoc:
     return (x['Ratings'])

#cautare dupa titlu
def cautare_dupa_titlu(title):
  myquery = {"Title": f"{title}"}
  mydoc = mycol.find(myquery)
  for x in mydoc:
    print(x)
#print(cautare_dupa_titlu("Titanic"))


def cautare_dupa_actor(actor):
  gasit=0
  for x in mycol.find():
    actors ={ "title": x['Title'],"actors": x['Actors'],"poster": x['Poster']}
    words = actors['actors'].split(', ')
    if actor in words:
        print(words)
        print(actors['title'],actors['poster'])
        gasit=1
  if(gasit==0):
    print("Nu s-a putu gasi film")

#print(cautare_dupa_actor('Kate Winslet'))

while True:
    clientsocket, addr = s.accept()
    print(f"Conexiunea cu {addr} a fost stabilita cu succes!")
    clientsocket.send(bytes("Bine ati venit", "utf-8"))
    msg = clientsocket.recv(4096)
    title = msg.decode("utf-8")
    print("Clientul doreste ratingul filmului: ", title)
    data = ratings(title)
    msg = pickle.dumps(data)
    print(msg)
    clientsocket.send(msg)
    #print(type(data))
    #print(data)







