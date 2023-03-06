import socket

port = 10500

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
    #print(f'Recebido: {data.decode()}')

    msg = input(': ')
    conn.send(msg.encode())
#Encerra a conexão
conn.close()
