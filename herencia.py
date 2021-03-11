class Madre(object):
    def __init__(self, parametro_1):
        self.par_1 = parametro_1
        
    def metodo_1(self):
        print('Metodo 1 de la clase madre')    
        
    def metodo_2(self):
        print('Metodo 2 de la clase madre')
        
#print(dir(Madre))      
#objeto_madre = Madre('Madre1')

class Hija(Madre):
    def metodo_1(self):
        print("Metodo 1 de la clase hija")
    
 
#print(dir(Hija))         
objeto_hija = Hija(24)
print(objeto_hija.par_1)
objeto_hija.metodo_1() #Metodo que se reescribio en la clase hija
objeto_hija.metodo_2() #Metodo que No se reescribio


            