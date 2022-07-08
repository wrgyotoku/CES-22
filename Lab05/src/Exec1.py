import tkinter as tk
from abc import abstractmethod

#Class to command

class Command():

    @abstractmethod
    def depositvalue(self,user,value):
        pass

    @abstractmethod
    def withdrawvalue(self,user,value):
        pass

    @abstractmethod
    def Transfer(self,send,receive,userslist,value):
        pass

    @abstractmethod
    def changeclient(self,user,substituteuser):
        pass

    @abstractmethod
    def checkbalance(self,user):
        pass

    
# Receiver
class Bankaccount():
    def __init__(self, name,initialvalue = 0):
        self.value = initialvalue
        self.name = name
    
    def balance(self):
        return(self.value)

    def deposit(self, value):
        self.value += value
        
    def withdraw(self,value):
        if (value< self.value):
            self.value -= value
            return True
        else:
            return False

class depositvalue(Command):
    def __init__(self):
        self.phrase = str("Deposito de: ")

    def depositvalue(self,user,value):
        user.deposit(value)
        return str(f"{self.phrase}" f"{value}" f".")

class Veriryingbalance(Command):
    def __init__(self):
        self.phrase = str("Saldo atual: ")

    def checkbalance(self,user):
        return str(f"{self.phrase}" f"{user.balance()}" f".")            

    
class withdrawvalue(Command):
    def __init__(self):
        self.phrase = str("Saque de: ")
        self.error = str("Saldo nao suficiente...")

    def withdrawvalue(self,user,value):
        self.positivebalance = user.withdraw(value)
        if (self.positivebalance):
            return str(f"{self.phrase}" f"{value}")
        else:
            return self.error

class changeclient(Command): 
    def __init_(self):
        self.error = str("Usuario nao encontrado!")

    def changeclient(self,user,substituteuser):
        if(substituteuser != 0):
            return substituteuser
        else:
            return user

class Transfer(Command):
    def __init__(self):
        self.phrase = str("Transferencia de: ")
        self.error = str("Saldo nao suficiente...")

    def Transfer(self,send,receive,value):
        self.positivebalance = send.withdraw(value)
        if (self.positivebalance):
            receive.deposit(value)
            return str(f"{self.phrase}" f"{value}")
        else:
            return self.error
               

#invoker how appear the command
class Application(tk.Frame):
    def __init__(self, master=None):

        super().__init__(master)
    
        self.master.title("Banco Yano")
        self.pack()
        self.master = master
        self.master.geometry("700x600")

        #Clients
        self.user1 = Bankaccount("Ryu",700)
        self.user2 = Bankaccount("Joao",1400)
        self.user3 = Bankaccount("Maria",1)
        self.userslist = [self.user1, self.user2, self.user3]

        # client who will be logged into the system 
        self.loggedclient = self.user1         
        self.register = "Registro de Atividades:"
        self.create()
        self.loginclient()
               
        
    def loginclient(self):
        self.label_logged['text']= str(f"Cliente: " f"{self.loggedclient.name}")

    def att_register(self,phrase):
        self.register +="\n"+phrase
        self.label_transactiondone['text'] = self.register

    #Buttons that you can use on window
    def create(self):
        #buttons
        self.button_depositvalue = tk.Button(self,text = "Deposito ",command = self.depositvalue)
        self.button_withdrawvalue = tk.Button(self,text = "Sacar",command = self.retiravalue)
        self.button_Transfer = tk.Button(self,text = "Transferir", command = self.transferevalue)
        self.button_changeuser = tk.Button(self,text = "Trocar usuario", command = self.changeuser)
        self.button_Veriryingbalance = tk.Button(self,text = "Saldo Atual",command = self.Veriryingbalance)
        
        #labels
        self.label_logged = tk.Label(self,text = "Usuario logado: ")
        self.label_transactiondone = tk.Label(self,text = self.register)
        self.label_value_deposit = tk.Label(self,text = "Valor em R$: ")
        self.label_user = tk.Label(self,text = "Transferir para o Usuario:")
        
        #entry
        self.entry_newuser = tk.Entry(self)
        self.entry_value_deposit = tk.Entry(self)
        self.entry_value_withdraw = tk.Entry(self)
        self.entry_value_transf = tk.Entry(self)
        self.entry_users = tk.Entry(self)

        #Disposition the buttons on screen
        self.label_logged.grid(row=0,column=1)
        self.button_changeuser.grid(row=2,column=0)
        self.entry_newuser.grid(row=2,column=1)  
        self.button_Veriryingbalance.grid(row=2,column=3)
        self.button_depositvalue.grid(row=6,column=0)
        self.label_value_deposit.grid(row=5,column=1)
        self.entry_value_deposit.grid(row=6,column=1)
        self.button_withdrawvalue.grid(row=8,column=0)
        self.entry_value_withdraw.grid(row=8,column=1)
        self.button_Transfer.grid(row=10,column=0)
        self.entry_value_transf.grid(row=10,column=1)
        self.label_user.grid(row=9,column=2)
        self.entry_users.grid(row=10,column=2)
        self.label_transactiondone.grid(row=12,column=1)

    #Warnings
    def changeuser(self):
        entry = self.entry_newuser.get()
        user = self.searchuser(entry)
        print(entry)
        command = changeclient()
        change = command.changeclient(self.loggedclient,user)
        if (change == self.loggedclient):
            phrase = str("Falha! mudanca nao executada.")
        else:
            self.loggedclient = user
            phrase = str("Usuario trocado")
        self.loginclient()
        #self.label_transactiondone['text'] = phrase
        self.att_register(phrase)

    def depositvalue(self):
        command = depositvalue()
        entry = float(self.entry_value_deposit.get())
        phrase = command.depositvalue(self.loggedclient,entry)
        self.att_register(phrase)

    def retiravalue(self):
        command = withdrawvalue()
        entry = float(self.entry_value_withdraw.get())
        phrase = command.withdrawvalue(self.loggedclient,entry)
        self.att_register(phrase)

    def Veriryingbalance(self):
        command = Veriryingbalance()
        phrase = command.checkbalance(self.loggedclient)
        self.att_register(phrase)

    def transferevalue(self):
        entry = self.entry_users.get()
        user = self.searchuser(entry)
        if(user == 0):
            phrase = str("Nao foi realizada a transferencia.")
        else:
            entry2 = float(self.entry_value_transf.get())
            command = Transfer()
            phrase = command.Transfer(self.loggedclient,user,entry2)
        self.att_register(phrase)
        
    def searchuser(self,entry):
        for user in self.userslist:
            if(entry == user.name):
                return user
        return 0
    
#To simulate the command
root = tk.Tk()
app = Application(master=root)
app.mainloop()