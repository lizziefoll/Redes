//calculadora do servidor
import socket

port = 20789

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0', port))
server.listen()

while True:
    print(f'=== Servidor aguardando conexões na porta {port}===')
    conn, addr = server.accept()
    print(f'Conexão recebida de {addr}')
    

#Recebe os dados enviados pelo cliente
    data = conn.recv(4096)
    msg = data.decode()

    msg = msg.split()
    if msg[1] == '+': 
        msg = int(msg[0])+int(msg[2])
        print(msg)
    elif msg[1] == '-':
        msg = int(msg[0])-int(msg[2])
        print(msg)
    elif msg[1] == '*': 
        msg = int(msg[0])*int(msg[2])
        print(msg)
    elif msg[1] == '/': 
        msg = int(msg[0])/int(msg[2])
        print(msg)

    x = str(msg)     
        
    conn.send(x.encode())
    #Encerra a conexão
    conn.close()
