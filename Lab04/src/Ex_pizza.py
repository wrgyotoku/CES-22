#(2) Crie um exemplo que construa Pizzas.

class PrimePizza:

    def get_custo(self):
        return self.__class__.custo

    def get_tipo(self):
        return self.__class__.__name__
    
# Classe Decorator
class Decorator(PrimePizza):

    def __init__(self,PrimePizza):
        self.componente = PrimePizza

    def get_custo(self):
        return self.componente.get_custo()+PrimePizza.get_custo(self)

    def get_tipo(self):
        return self.componente.get_tipo() + ' ' + PrimePizza.get_tipo(self)

#Classe Massa com seu custo
class Massa(PrimePizza):
    custo = 7.0

#Classes com diferentes igredientes de pizza com seus custos:
class Queijo(Decorator):
    custo = 3.0
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)

class Cebola(Decorator):
    custo = 1.0
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)

class Presunto(Decorator):
    custo = 2.0
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)

class Tomate(Decorator):
    custo = 1.0
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)

class Milho(Decorator):
    custo = 0.5
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)

class Ovo(Decorator):
    custo = 2.5
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)

class Ervilha(Decorator):
    custo = 2.7
    def __init__(self,PrimePizza):
        Decorator.__init__(self,PrimePizza)


#Simulação de pedido de pizza:

ModaCasa = Queijo(Tomate(Ervilha(Massa())))
print("Pizza ModaCasa:  nela usou-se " + ModaCasa.get_tipo()+ "\nValor Total: R$"+str(ModaCasa.get_custo()))
print("************************************************************")
Portuguesa = Queijo(Milho(Cebola(Massa())))
print("Pizza Portuguesa: nela usou-se " + Portuguesa.get_tipo()+ "\nValor Total: R$"+str(Portuguesa.get_custo()))
print("************************************************************")
SeuJeito = Queijo(Presunto(Ovo(Massa())))
print("Pizza do SeuJeito: nela usou-se " + SeuJeito.get_tipo()+ "\nValor Total: R$"+str(SeuJeito.get_custo()))