'''
Encapsulamiento
'''
class OcultaX(object):
    def __init__(self):
        self.__x = 5
        
    def mostrar_x(self):
        return self._OcultaX__x
    
    def incrementa_x(self):
        self._OcultaX__x+= 1

o = OcultaX()
#print(dir(o))  

print(o.mostrar_x())  
o.incrementa_x()
print(o.mostrar_x())   

o.incrementa_x()
print(o.mostrar_x())  

o.incrementa_x()
print(o.mostrar_x())   
        