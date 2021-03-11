'''
Herencia Multiple
'''
class A(object):
    def __init__(self):
        print('Contructor de la clase A')

class B(object):
    def __init__(self):
        print('Contructor de la clase B')
        
class C(A, B):
    pass

objeto_c = C()
                    