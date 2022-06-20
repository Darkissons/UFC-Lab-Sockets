import socket
import threading

def init():
    HOST = 'localhost'
    PORT = 50000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.connect((HOST, PORT))
    except:
        return print('Não foi possível se conectar ao servidor.')

    username = input()

    thread_1 = threading.Thread(target=receive, args=[server]).start()
    thread_2 = threading.Thread(target=send, args=[server, username]).start()

def receive(server):
    while True:
        try:
            msg = server.recv(2048).decode('UTF-8')
            print(msg+'\n')
        except:
            print('Conexão perdida!')
            server.close()
            break

def send(server, username):
    while True:
        try:
            msg = input()
            server.send(f'<{username}> {msg}'.encode('UTF-8'))
        except:
            return

init()