'''
Herencia y nuevos atributos del caso2

Caso 2: Reescribir el __init__(Funciona en el caso que sean pocos atributos)
'''
class Madre(object):
    def __init__(self, par):
        self.uno = par
        
class Hija(Madre):
    def __init__(self, par1, par2):
        super(Hija, self).__init__(par1)
        self.dos = par2
         
m = Madre('Madre')
h = Hija('Hija1', 'Hija2')   

print(f'Atributo de la Madre = {m.uno}')
print(f'Atributo uno de la hija = {h.uno}')   
print(f'Atributo dos de la hija = {h.dos}')