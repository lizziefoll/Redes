import socket 

port = 20789 #porta de conexão
dest = 'localhost' #'192.168.246.55' #ip da maquina

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== Conectando ao servidor {dest}:{port} ====')
client.connect((dest,port))


msg = input(': ')                 
client.send(msg.encode())
             
          
msg = client.recv(4096)
print(f'Servidor: {msg.decode()}')

client.close()
