import abc

class Oficina:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod # metodo abstrato
    def reparar_carro(self):
        """Method that should do something."""

    @classmethod
    @abc.abstractmethod # metodo abstrato
    def deu_problema(cls): #metodo de classe
        print("analisando problema")
        cls.ligar_para_suporte()

    
    def __init__(self, nmro_car):
        self.nmro_car = nmro_car

    def reparar_carro(self):
        print("reparou:",self.nmro_car,"carros")    

    '''escopo proprio nao possui acesso a classe ou a instancia'''
    @staticmethod
    def ligar_para_suporte(): #metodo estatico
        print("ligou para o mecanico")

    '''invocando staticmethod dentro de classmethod'''
    @classmethod
    def deu_problema(cls): #metodo de classe
        print("analisando problema")
        cls.ligar_para_suporte()

    '''invocando staticmethod dentro de instancia'''
    def consertar(self): #metodo de instancia
        print("consertou 1 carro")
        self.ligar_para_suporte()

#Testes
# nao possui acesso a classe ou a instancia
Oficina.ligar_para_suporte()

# nao necessita de objeto instanciado
Oficina.deu_problema()

# instanciando
oficina = Oficina(7)
# necessita de objeto instanciado
oficina.consertar()

oficina.reparar_carro()