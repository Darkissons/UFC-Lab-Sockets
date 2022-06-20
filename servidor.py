import socket
import threading

clients = []

def init():
    HOST = 'localhost'
    PORT = 50000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        server.listen()
        print('Servidor criado!')
    except Exception as e:
        return print('Não foi possível executar o servidor.', e)

    while True:
        conn, ender = server.accept()
        clients.append(conn)

        thread_1 = threading.Thread(target=messages, args=[conn]).start()

def messages(conn):
    while True:
        try:
            msg = conn.recv(2048)
            broadcast(msg, conn)
        except:
            clients.remove(conn)
            break

def broadcast(msg, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(msg)
            except:
                clients.remove(client)

init()