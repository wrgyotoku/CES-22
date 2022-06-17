from abc import abstractmethod

#(1) Utilize o Design Pattern Bridge para modelar estas classes. Implemente este 
#modelo de classes em Python. 

#Interface motor
class motor():
    @abstractmethod
    def get_consome(self) ->str:
        pass

# Classes inerentes à motorização:
class Combustao(motor):
    def __init__(self):
        self.consome = True
        self.nome = __class__.__name__
    def get_consome(self) -> str:
        return (f"{self.nome}"  f" consome muito, e eh caro.")

class Eletrico(motor):
    def __init__(self):
        self.consome = False
        self.nome = __class__.__name__
    def get_consome(self) -> str:
        return (f"{self.nome}"  f" consome pouco, e eh mais barato.")

class Hibrido(motor):
    def __init__(self):
        self.consome = False
        self.nome = __class__.__name__
    def get_consome(self) -> str:
        return (f"{self.nome}"  f" consome menos, e tem custo medio.")

#Interface Tipo_Veiculo
class Tipo_Veiculo():
    @abstractmethod
    def get_nome(self) ->str:
        pass

# Classes inerentes ao tipo de veiculo:
class Caminhao(Tipo_Veiculo):
    def __init__(self):
        self.nome = "Caminhao"
    def get_nome(self) -> str:
        return f"{self.nome}"

class Bicicleta(Tipo_Veiculo):
    def __init__(self):
        self.nome = "Bicicleta"
    def get_nome(self) -> str:
        return f"{self.nome}"

class Carro(Tipo_Veiculo):
    def __init__(self):
        self.nome = "Carro"
    def get_nome(self) -> str:
        return f"{self.nome}"

#Classe Veiculo
class Veiculo():
    def __init__(self,motor:motor,tipo2:Tipo_Veiculo):
        self.motor = motor
        self.tipo = tipo2
    def get_veiculo(self):
        print (f"{self.tipo.get_nome()}",f",cujo motor eh",f"{self.motor.get_consome()}")

#Interface Construtor
class Construtor():
    @abstractmethod
    def construir_veiculo(self):
        pass

class Constroi_carro(Construtor):
    def construir_veiculo(self):

        implementacao = Hibrido()

        implementacao2 = Carro()

        abstracao = Veiculo(implementacao,implementacao2)

        return abstracao

class Constroi_bicicleta(Construtor):
    def construir_veiculo(self):

        implementacao = Eletrico()

        implementacao2 = Bicicleta()

        abstracao = Veiculo(implementacao,implementacao2)

        return abstracao

class CriarCaminhao(Construtor):
    def construir_veiculo(self):

        implementacao = Combustao()

        implementacao2 = Caminhao()

        abstracao = Veiculo(implementacao,implementacao2)
        
        return abstracao



def cliente(Construtor):
    return Construtor.construir_veiculo()


#Simulando:

Bicicleta = cliente(Constroi_bicicleta())
print("O tipo de veiculo eh:")
Bicicleta.get_veiculo()
print("************************************************************")
Carro = cliente(Constroi_carro())
print("O tipo de veiculo eh:")
Carro.get_veiculo()
print("************************************************************")
Caminhao = cliente(CriarCaminhao())
print("O tipo de veiculo eh:")
Caminhao.get_veiculo()    