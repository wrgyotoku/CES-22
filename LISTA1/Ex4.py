#Ex.4
#Funcao que verifica se numero n eh primo
#Cujo parametro eh o inteiro n
def is_prime(n):
    #numero n eh diferente de 0 e 1 e negativo
    if n > 1:
        #Verifica casos se o numero eh divisivel por numero diferente dele mesmo e de 1
        for i in range(2, n):
            if (n % i) == 0:
                print ('False')
                break
        else:
            print ('True')
    # Caso o numero seja 0 ou 1 ou negativo
    else:
        print ('False')


#Teste da funcao
numero = is_prime(5)
###########################################