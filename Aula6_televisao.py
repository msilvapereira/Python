class Televisao:
    def __init__(self): #a televisão inicialmente está desligada, por isso recebe false
        self.ligada = False
        self.canal = 5
    
    def power(self): #o método power liga a televisão que inicialmente estava desligada (False)
        if self.ligada:
            self.ligada = False #o que antes estava desligada
        else:
            self.ligada = True #agora está ligada
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1 #irá aumentar o canal em + 1
    
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1 #irá diminuir o canal em - 1

televisao = Televisao()
print('Televisao esta ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))