
#Ex.3
#Funcao que retorna a soma de todos os números int de ateh n
# Paramentro inteiro n
def sum_to(n):
    a = 0
    for i in range(1,n+1):
        a = a + i
    return a


#Teste da funcao
soma = sum_to(10)
print(soma)
################################################