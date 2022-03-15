

#Ex.5
#Funcao cujo parametro eh uma string
def is_palindrom(string):
    #elimina espacos da string
    str = string.replace(' ','')
    #inverte a string
    frase_invert = str[::-1]
    #compara se str igual sua invertida
    if str == frase_invert:
        print ('Eh palindromo')
    else:
        print('Nao eh palindromo')


# Teste de casos como 'apos a sopa','123321','ovo'
is_palindrom(' 123321')