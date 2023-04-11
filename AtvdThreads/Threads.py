from threading import Thread
from time import sleep 


class Contador(Thread): 
    def __init__(self,n, segundos, nome): 
        Thread.__init__(self)
        self.n = n
        self.segundos = segundos
        self.nome = nome

    def run(self): 
        for i in range(self.n):
            print(i+1)
            sleep(self.segundos)
        print(f'Contador de {self.nome} finalizado.')

Contador(5,2, 'Guilhermina').start()#contador rxecuta o __init__ e start executa o run 
Contador(10,2, 'Josefh').start()#(10,3)- 10 é o numeros printados no intervalo de 2 segundos
Contador(15, 1, 'Magaiver').start()

# print('aguardando threads terminarem')
# sleep(15)
# print('Programa finalizado')
