from abc import ABCMeta, abstractmethod

#(2) Modele o problema usando o padrão Builder. 
class PrimeBoloBuilder(metaclass=ABCMeta):
    #Builder Interface do Bolo

    @staticmethod
    @abstractmethod
    def set_tipo_bolo(tipo_bolo):
        "Tipo do bolo"

    @staticmethod
    @abstractmethod
    def set_quantidade_bolo(quantidade):
        "Quantidade do bolo"

    @staticmethod
    @abstractmethod
    def set_estilo_bolo(estilo_bolo):
        "Estilo do bolo"

    @staticmethod
    @abstractmethod
    def get_resultado():
        "Resultado final"

class BoloBuilder(PrimeBoloBuilder):
    #Builder Bolo

    def __init__(self):
        self.bolo = Bolo()

    def set_tipo_bolo(self, tipo_bolo):
        self.bolo.tipo_bolo = tipo_bolo
        return self

    def set_quantidade_bolo(self, quantidade):
        self.bolo.quant = quantidade
        return self

    def set_estilo_bolo(self, estilo_bolo):
        self.bolo.estilo_bolo = estilo_bolo
        return self

    def get_resultado(self):
        return self.bolo

#Produto
class Bolo():  

    def __init__(self, tipo_bolo=None, quant=0,
                 estilo_bolo=None):
       
        self.tipo_bolo = tipo_bolo
        self.quant = quant     
        self.estilo_bolo = estilo_bolo

    def elaboracao(self):

        return f"Voce encomendou: {self.quant} bolo(s) "\
            f"de {self.estilo_bolo} do delicioso tipo {self.tipo_bolo}."


class Chocolate:  

    @staticmethod
    def construtor():
      
        return BoloBuilder()\
            .set_tipo_bolo("de Chocolate")\
            .set_estilo_bolo("Casamento")\
            .set_quantidade_bolo(1)\
            .get_resultado()


class Mandioca:  

    @staticmethod
    def construtor():
      
        return BoloBuilder()\
            .set_tipo_bolo("de Mandioca")\
            .set_estilo_bolo("Festa Informal")\
            .set_quantidade_bolo(7)\
            .get_resultado()


class Cenoura:  

    @staticmethod
    def construtor():
        
        return BoloBuilder()\
            .set_tipo_bolo("de Cenoura")\
            .set_estilo_bolo("Aniversario")\
            .set_quantidade_bolo(5)\
            .get_resultado()



#Simulação
CHOCO = Chocolate.construtor()

CENOURA = Cenoura.construtor()

MANDIOCA = Mandioca.construtor()

print(CHOCO.elaboracao())
print("\n**********************************************************************")
print(CENOURA.elaboracao())
print("\n***********************************************************************")
print(MANDIOCA.elaboracao())  
print("\n************************************************************************")