
class Livro(object):
    
    def __init__(self,titulo,Autor,genero, edicao,editora,precoVenda,precoCompra):
        self.titulo = titulo
        self.Autor = Autor
        self.genero = genero
        self.edicao = edicao      
        self.editora = editora
        self.precoVenda = precoVenda
        self.precoCompra = precoCompra
        
    def get_titulo(self):
        return self.titulo
    def get_Autor(self):
        return self.Autor
    def get_genero(self):
        return self.genero    
    def get_edicao(self):
        return self.edicao   
    def get_editora(self):
        return self.editora
    def get_precoVenda(self):
        return self.precoVenda
    def get_precoCompra(self):
        return self.precoCompra
    def __str__(self):
        return "titulo: " + self.titulo + " \nAutor: " + self.Autor +  " \ngenero:" + self.genero + " \nedicao:" + self.edicao +" \neditora:" + str(self.editora) + " \nprecoVenda:" + str(self.precoVenda) + " \nprecoCompra:" + str(self.precoCompra) 
        

class Autor(object):
    def __init__(self, nome, publicados):
        self.nome = nome
        self.publicados = publicados

    def get_publicados(self):
        for publicou in self.publicados:
            str(publicou)
    
    def __str__(self):
        return self.nome


class Cliente(object):
    def __init__(self, nome, email):
        self.nome = nome       
        self.email = email
        self.compraPassada = []
        
    def get_nome(self):
        return self.nome
    
    def get_email(self):
        return self.email
    
    def get_compraPassada(self):
        if(self.compraPassada == []):
            return print("Cliente nao tem compra passada")
        for indice,compra in enumerate(self.compraPassada): 
            print("compra " + str(indice +1) + ":")
            print(compra)
            print("*************************************")
    
    def insercao_compra(self, compra):
        self.compraPassada.append(compra)
        
    def remocao_compra(self, compra):
        if(compra in self.compraPassada):
            self.compraPassada.remocao(compra)
        else:
            print("compra nao encontrada")  

    def __str__(self):
        return "nome: " + self.nome +  " \n email: " + self.email         





class Livraria(object):
    def __init__(self, Clientes, Livros,Autor):
        self.Clientes = Clientes
        self.Livros = Livros
        self.Autor = Autor
     
    def get_Clientes(self):
        if(self.Clientes == []):
            return print("Livraria nao tem Clientes")
        print("Clientes:")
        
        for indice,Cliente in enumerate(self.Clientes):
            if(Cliente != None):
                print("Cliente " + str(indice +1) + ":")
                print(Cliente)
                print("***************************")
    
    def get_Livros(self):
        if(self.Livros == []):
            return print("Livraria nao tem Livros")
        print("Livros:")
        
        for indice,Livro in enumerate(self.Livros):
            if(Livro != None):
                print("Livro " + str(indice +1) + ":")
                print(Livro)
                print("*******************************")
    
    def get_Autor(self):
        if(self.Autor == []):
            return print("Livraria nao tem Autor")
        print("Autor:")
        
        for indice,Autor in enumerate(self.Autor):
            if(Autor != None):
                print("Autor " + str(indice +1) + ":")
                print(Autor)
                print("*******************************")



    ## Operacao Livros,Clientes,Autores, Compras
    ##################################################

    def insercao_Livro(self, Livro):
        self.Livros.append(Livro)
    
    def remocao_Livro(self, Livro):
        if(Livro in self.Livros):
            self.Livros.remocao(Livro)
        else:
            print("Livro nao existe")    
    
    def consulta_Livro(self, Livro):
        if(Livro in self.Livros):
            return print("***************\n" + str(self.Livros[self.Livros.indice(Livro)]) + "\n***************")
        return print("Livro nao existe")

    def insercao_Cliente(self, Cliente):
        self.Clientes.append(Cliente)
        
    def consulta_Cliente(self, Cliente):
        if(Cliente in self.Clientes):
            return print("*************** \n" + str(self.Clientes[self.Clientes.indice(Cliente)]) + "\n***************")
        return print("Cliente nao existe")
    
    def remocao_Cliente(self, Cliente):
        if(Cliente in self.Clientes):
            self.Clientes.remocao(Cliente)
        else:
            print("Cliente nao existe")
           
    def insercao_Autor(self, Autor):
        self.Autor.append(Autor)    
    
    def remocao_Autor(self, Autor):
        if(Autor in self.Autor):
            self.Autor.remocao(Autor)
        else:
            print("Autor nao existe")
                
    def consulta_Autor(self, Autor):
        if(Autor in self.Autor):
            return print("*************** \n" + str(self.Autor[self.Autor.indice(Autor)]) + "\n***************")
        return print("Autor nao existe")    

    # def insercao_Compra(self, compra):
    #     self.compra.append(compra)
    
    # def remocao_Compra(self, compra):
    #     if(compra in self.compra):
    #         self.compra.remocao(compra)
    #     else:
    #         print("Compra nao existe")    
    
    # def consulta_Compra(self, compra):
    #     if(compra in self.compra):
    #         return print("***************\n" + str(self.compra[self.compra.indice(Livro)]) + "\n***************")
    #     return print("Compra nao existe")    



class compra:
    def __init__(self, Cliente, Livro):
        self.Cliente = Cliente
        self.Livro = Livro
        self.insercao_compra(Cliente,Livro)
    def __str__(self):
        return "compra: \nCliente: " + str(self.Cliente) + "\nLivro: " + str(self.Livro) 
    
    def insercao_compra(self, Cliente, compra):
        Cliente.insercao_compra(compra)
        
    def remocao_compra(self, Cliente, compra):
        Cliente.remocao_compra(compra)    
    
    def get_Livro(self):
        return self.Livro





#Livraria
Saraiva = Livraria([],[],[])

#Livros
Quimica = Livro("Principios de Quimica", "Peter Atkins", "Exatas", '3', "Bookman",'300', '100')
Fisica = Livro("Fisica Classica", "Caio Sergio Calcada", "Exatas", '4', "Atual",'100','50')

#Autores
Atkins = Autor("Peter Atkins", [Quimica])
Calcada = Autor("Caio Sergio Calcada", [Fisica])

#Clientes
Ryu = Cliente("Ryu", "1531@gmail.com")
Yano = Cliente("Yano", "hash51514@gmail.com")



# insercao de livros
Saraiva.insercao_Livro(Quimica)
Saraiva.insercao_Livro(Fisica)

# insercao de autores
Saraiva.insercao_Autor(Atkins)
Saraiva.insercao_Autor(Calcada)

# insercao de clientes
Saraiva.insercao_Cliente(Ryu)

# Listas
Saraiva.get_Livros()

Saraiva.get_Autor()

Saraiva.get_Clientes()



