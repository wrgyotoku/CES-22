class Animal:

    def __init__(self, genero, cor_pelo):
        self.genero = genero
        self.cor_pelo = cor_pelo

    def faz_som(self):
        print("Som de animal")

class Domesticado:
    def esta_dormindo(self):
        print("Domesticado gosta de dormir")

class Mamifero(Animal):
    pass

#Heranca Multipla
class Cachorro(Mamifero, Domesticado):
    def osso(self):
        print("Cao gosta de enterrar osso")

class Lobo(Mamifero):
    def faz_som(self):      
       print("Lobo uiva")

class Pessoa(Animal):
    def __init__(self, cabelo):
        self.cabelo = cabelo
    def fala(self):    
        print("Sou uma pessoa e sou capaz de falar")

# Super
class Humano(Animal):
    def __init__(self, genero, cor_pelo, cabelo):
        super(Humano,self).__init__(genero, cor_pelo)
        self.cabelo = cabelo


# Testes
osmar = Humano('masculino', 'preto', 'castanho')

print(osmar.cabelo)

print(osmar.cor_pelo)
# chamou funcao da superclasse
osmar.faz_som()

julio = Pessoa('Loiro')

julio.fala()

lobo = Lobo('femea','rosa')

lobo.faz_som()

cachorro = Cachorro('macho','azul')

cachorro.faz_som()

cachorro.esta_dormindo()

cachorro.osso()

rex = Animal ('macho', 'marrom')

rex.faz_som()

