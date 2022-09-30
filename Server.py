import socket

HEADER = 1024
PORT = 3002
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        #msg_length = conn.recv(HEADER).decode(FORMAT)
        msg = conn.recv(HEADER).decode(FORMAT)
        #print(msg)
        if msg:
            if msg == DISCONNECT_MESSAGE:
                connected = False

            filename = msg.split()[1]
            filename = filename[1:]
            print(filename)
            try:
                    f = open(filename)
                    response_body = f.read()
                    response_header = "HTTP/1.1 200 OK\r\n"
                    response = response_header +"\r\n" + response_body
                    #print(response)
                    conn.send(bytes(response,FORMAT))   
                    connected = False   
            except:
                conn.send("HTTP/1.1 404 Not Found\n\n".encode(FORMAT))
                print("file not found 404")
                connected = False 

def start():
    server.listen(1)
    print(f"[LISTENING] WebServer is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        handle_client(conn,addr)
        conn.close()

print("[STARTING] server is starting...")
start()