class Saludo(object):
    nombres = 'Francisco Javier'
    apellidos = 'Murillo Vasquez'
    Direccion = "Managua, Nicaragua"
    
    def saludar(self):
        print(f"Hola Soy:{self.nombres} {self.apellidos} {self.Direccion}")
        
objeto = Saludo()
objeto.saludar()  

objeto_2 = Saludo()
objeto_2.nombres = "MariaJose"
objeto_2.apellidos = "Ruiz Garcia"
objeto_2.Direccion = "Masaya, Nicaragua"
objeto_2.saludar()     
    
     