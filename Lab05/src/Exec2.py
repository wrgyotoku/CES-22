from abc import abstractmethod


#Documento
class Document():

    def __init__(self,initial_state,user):
        self.changeState(initial_state)
        self.autor = user

    def changeState(self,state):
        self._state = state
        self._state.document = self
        print("************* Foi para o estado " + state.__name__+"*************")

    def failreview(self,user):
        self._state.failreview(user)

    def expire(self):
        self._state.expire()

    def render(self,user):
        self._state.render(user)

    def publish(self,user):
        self._state.publish(user)  

# Estados: Draft, moderation, published
class State():

    @abstractmethod
    def publish (self,user):
        pass

    @abstractmethod
    def failreview(self,user):
        pass

    @abstractmethod
    def expire(self):
        pass

    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, document: Document) -> None:
        self._document = document

    @abstractmethod
    def render(self,user):
        pass
    

#Usuario
class User():
    def __init__(self,name):
        self.isAdmin = False
        self.name = name

    def setAdmin(self):
        self.isAdmin = True


'''A seguir os estados do documento'''
#Rascunho
class Draft(State):
    def __init__(self):
        self.__name__ = self.__class__.__name__

    def publish(self,user):
        if(user == self.document.autor):
            self.document.changeState(Moderation())
        elif(user.isAdmin):
            self.document.changeState(Published())
        else:
            print(user.name + " sem credenciais para publicar o referido documento")

    def render(self,user):
        if(user.isAdmin or user == self._document.autor):
            print("Autorizado mostrar esse documento.")
        else:
            print(user.name + " sem credenciais para o referido documento")
    
    

#Publicado
class Published(State):
    def __init__(self):
        self.__name__ = self.__class__.__name__
    
    def publish(self,user):
        if(user == self.document.autor):
            self.document.changeState(Moderation())
        elif(user.isAdmin):
            self.document.changeState(Published())
        else:
            print("Sem credenciais para publicar o referido  documento")
    
    def expire(self):
        print("Documento expirado")
        self.document.changeState(Draft())

    def render(self,user):
        if(user.isAdmin or user == self._document.autor):
            print("Autorizado mostrar esse documento.")
        else:
            print(user.name+" Sem credenciais para ver o referido documento")    

#Moderação
class Moderation(State):
    def __init__(self):
        self.__name__ = self.__class__.__name__
    
    def publish(self,user):
        if(user == self.document.autor):
            print("O documento esta sobre moderacao. ")
        elif(user.isAdmin):
            self.document.changeState(Published())
        else:
            print("Sem credenciais para publicar o referido documento")

    def render(self,user):
        if(user == self._document.autor):
            print("O documento esta sobre moderacao.")
        elif(user.isAdmin):
            print("Pode ver o documento")
        else:
            print("Sem credenciais para ver o referido documento")
    
    def failreview(self,user):
        if(user.isAdmin):
            print("O documento de "+self.document.autor.name+" nao foi aceito para ser publicado.")
            self.document.changeState(Draft())
        else:
            print("Sem credenciais para tal comando")



###########################################################
#Simulação

#Autor
Yano = User("Yano")
#Nao possui credenciais 
Ryu = User("Ryu")
Joao = User("Joao")
#Admin
Joao.setAdmin()

initial_state = Draft()
documento = Document(initial_state,Yano)
documento.render(Ryu)
documento.render(Yano)
documento.render(Joao)
documento.publish(Ryu)
documento.publish(Yano)
documento.failreview(Joao)
documento.publish(Joao)
documento.expire()