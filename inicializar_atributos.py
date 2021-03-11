"""
    Inicializar atributos
    
    Metodo__init__
"""
class calculadora(object):
    def __init__(self, operando_1, operando_2):
        self.op_1 = operando_1
        self.op_2 = operando_2
        
    def sumar(self):
        return self.op_1 + self.op_2
    
    def restar(self):
        return self.op_1 - self.op_2
    
    def multiplicar(self):
        return self.op_1 * self.op_2
    
    def dividir(self):
        return self.op_1 / self.op_2    
    
o = calculadora(10, 2)
print(o.sumar())    
print(o.restar())
print(o.multiplicar())
print(o.dividir())

o2 = calculadora(20, 5)
print(o2.sumar())    
print(o2.restar())
print(o2.multiplicar())
print(o2.dividir())