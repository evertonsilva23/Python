# O programa a seguir conta o número de vezes que a letra “a” aparece em uma
# string:
# palavra = 'banana'
# contagem = 0
# for letra in palavra:
# if letra == 'a':
# contagem = contagem + 1
# print(contagem)
# Esse programa demonstra outro padrão da computação chamado contador. A
# variável contagem é inicializada com 0 e então incrementada a cada vez que um
# “a” é encontrado. Quando o laço acaba, contagem tem como resultado o número
# total de a’s.
# Exercício 3: Encapsule esse código em uma função chamada contagem,
# e generalize para que ela aceite a string e a letra como argumentos.


def count(palavra, pesquisa):
    contagem = 0
    for letra in palavra:
        if letra == pesquisa:
            contagem = contagem + 1
    print(contagem)
    
count("banana", "n")