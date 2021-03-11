'''
Herencia y nuevos atributos

Caso 1: Reescribir el __init__(Funciona en el caso que sean pocos atributos)
'''
class Madre(object):
    def __init__(self, par):
        self.uno = par
        
class Hija(Madre):
    def __init__(self, par_1, par_2):
         self.uno = par_1
         self.dos = par_2
         
m = Madre('Madre')
h = Hija('Hija1', 'Hija2')   

print(f'Atributo de la Madre = {m.uno}')
print(f'Atributo uno de la hija = {h.uno}')   
print(f'Atributo dos de la hija = {h.dos}')
            