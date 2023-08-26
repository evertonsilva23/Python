# Exercício 1: Escreva uma função chamada corte que recebe uma lista e
# a modifica, removendo o primeiro e o último elemento, e retorna None.
# Depois escreva uma função chamada meio que recebe uma lista e retorna
# uma nova lista que contém todos, menos o primeiro e o último elemento.


#Definindo a funcao
def corte(a):
    b = a[1:len(a)-1]
#Chamando a funcao e imprimindo    
lista = [1,2,3,4,5]
print(corte(lista))

