from abc import ABCMeta, abstractmethod

#(1) Modele o problema usando o padrão Fábrica Abstrata
class Bolo(metaclass=ABCMeta):
#Interface Bolo

    @staticmethod
    @abstractmethod
    def get_tipo():
        "Metodo estatico para interface"

#Tipo Bolo de Chocolate
class Chocolate(Bolo):  

    def __init__(self):
        self._estilo = "de Casamento"
        self._cobertura = "Chantily"
        self._quantidade = 1

    def get_tipo(self):
        return {
            "cobertura": self._cobertura,
            "quantidade": self._quantidade,
            "estilo": self._estilo
        }

#Tipo Bolo de Mandioca
class Mandioca(Bolo):  

    def __init__(self):
        self._estilo = "de Festa Informal"
        self._cobertura = "Sem cobertura"
        self._quantidade = 3

    def get_tipo(self):
        return {
            "cobertura": self._cobertura,
            "quantidade": self._quantidade,
            "estilo": self._estilo
        }

#Tipo Bolo de Cenoura
class Cenoura(Bolo):  

    def __init__(self):
        self._estilo = "de Aniversario"
        self._cobertura = "Ganache"
        self._quantidade = 7

    def get_tipo(self):
        return {
            "cobertura": self._cobertura,
            "quantidade": self._quantidade,
            "estilo": self._estilo
        }
                                
class BoloFactory:  

    @staticmethod
    def get_bolo(bolo):
                
        if bolo == 'Cenoura':
            return Cenoura()
        if bolo == 'Mandioca':
            return Mandioca()
        if bolo == 'Chocolate':
            return Chocolate()
        else:
            return None      

#Padaria    
class PrimePadariaFactory(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def get_padaria(padaria):
        "Metodo estatico para fabrica abstrata"

class PadariaFactory(PrimePadariaFactory):
    
    @staticmethod
    def get_padaria(padaria):
                
        if padaria in ['Chocolate', 'Mandioca', 'Cenoura']:
            return BoloFactory().get_bolo(padaria)
        else:
            return None



#Simula o uso do padaria
padaria = PadariaFactory.get_padaria("Chocolate")
print("Voce solicitou Bolo: ")
print(padaria.__class__)
print("Com as seguintes especificacoes: ")
print(padaria.get_tipo())
print("************************************************************************")       

padaria = PadariaFactory.get_padaria("Cenoura")
print("Voce solicitou Bolo: ")
print(padaria.__class__)
print("Com as seguintes especificacoes: ")
print(padaria.get_tipo())
print("************************************************************************") 

padaria = PadariaFactory.get_padaria("Mandioca")
print("Voce solicitou Bolo: ")
print(padaria.__class__)
print("Com as seguintes especificacoes: ")
print(padaria.get_tipo())
print("*********************************************************************************") 

