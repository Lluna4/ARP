from logging import error
import socket
import threading
#import telebot
import asyncio
import csv

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!desconectar"

#bot = telebot.AsyncTeleBot("1695155940:AAGntm1f5wrH7fM4N6JVWSrD552xekryTDs", parse_mode=None)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

c = False
c2 = 0
a = True


clients = [] 
clients_lock = threading.Lock()

def a_False():
    a = False

def bot2(conn, addr):
    conectado = True
    usuario = ""
    while conectado == True:
        
        msg = conn.recv(1024).decode(FORMAT)
        for client in clients:
            client.send(msg.encode(FORMAT))
            tt = threading.Timer(5, a_False)
            while a == True:
                tt.start()
                msg4 = conn.recv(1024).decode(FORMAT)
                with open("arp.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow([msg, msg4])






                


   

def start():
    global c
    server.listen()

    print(f"El servidor acepta nuevas conexiones en {SERVER}")
    while True:
        conn, addr = server.accept()
        print("si")
        if c == False:
            x2 = threading.Thread(target=bot2, args=(conn, addr))
            x2.start()
            
        
        clients.append(conn)
        print(type(clients))
        print(clients)
    
          
    



print("El servidor se esta iniciando")


x1 = threading.Thread(target=start)

x1.start()