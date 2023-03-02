import socket 

port = 10500 #porta de conexão
dest = 'localhost' #'192.168.246.55' #ip da maquina

#msg = '90 anos, eu faço a minha calçada, eu faço e ele quebra, eu faço e ele quebra denovo'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== Conectando ao servidor {dest}:{port} ====')
client.connect((dest,port))

while True: 
    msg = input(': ')
    client.send(msg.encode())

    msg = client.recv(4096)
    #print(f'Servidor: {msg.decode()}')

client.close()
