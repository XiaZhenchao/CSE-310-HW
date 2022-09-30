import socket
import sys
from unicodedata import name
import os.path
# Receive secletting
RECEIVE_HEADER = 1024
RECEIVE_PORT = 5058
SERVER = socket.gethostbyname(socket.gethostname())
RECEIVE_ADDR = (SERVER,RECEIVE_PORT)

#General setting
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

receive_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
receive_server.bind(RECEIVE_ADDR)


def RemoveAdditionalCharacter(filename):
    if "http:" in filename:
        filename = filename.replace("http:","")
    if "/" in filename:
        filename = filename.replace("/","")
    print(filename)
    return filename

def SaveInCache(filename,content):
    print("SaveInCache")
    if "html" not in filename:
        filename = filename + ".html"
    File = open(filename,'w')
    File.writelines(content.decode())
    File.close()


def LoadFromCache(filename):
    print("LoadCache")
    try:
        file = open(filename)
        content = file.read().encode()
        file.close()
    except IOError:
        return None
    return content



def handle_clientRecieve(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(RECEIVE_HEADER).decode(FORMAT)
        Target = msg.split("\n")[0]
        Target = Target.split(" ")[1][1:]
        #Example: http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
        TargetName = Target
        if "//" in Target:
            SlashIndex = Target.index("/")
            #remove http//
            Target = Target[SlashIndex+1:]
            SlashIndex = Target.index("/")
            Target = Target[SlashIndex+1:]
        if "/" in Target:
            SlashIndex = Target.index("/")
            host = Target[0:SlashIndex]
            TargetUrl = Target[SlashIndex:]
        else:
            host = Target
            TargetUrl = "/"
        print("host: "+host)
        TargetName =  RemoveAdditionalCharacter(TargetName)
        print("TargetName: "+ TargetName)
        file_exists = os.path.exists(TargetName)
        send_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        request_header = "GET "+TargetUrl +" " + "HTTP/1.1\r\nHost: "+host+"\r\n\r\n"
        if file_exists:
            website = LoadFromCache(TargetName)
        else:
            send_server.connect((socket.gethostbyname(host),80))
            #request_header = "GET /wireshark-labs/HTTP-wireshark-file4.html " + "HTTP/1.1\r\nHost: "+"gaia.cs.umass.edu"+"\r\n\r\n"
            send_server.sendall(request_header.encode())
            send_server.settimeout(0.5)
            message = send_server.recv(4096)
            website=message
            while len(message)>0:
                try:
                    message=send_server.recv(4096)
                    website+=message
                except socket.timeout as e:
                    break    
            SaveInCache(TargetName,website)
        conn.sendall(website)  
        connected = False
        send_server.close()
        sys.exit(0)
def start():
    receive_server.listen(1)
    print(f"[LISTENING] ProxyServer is listening on {SERVER}")
    #listen from client
    while True:
        conn, addr = receive_server.accept()
        handle_clientRecieve(conn,addr)
        conn.close()

print("[STARTING] server is starting...")
start()




