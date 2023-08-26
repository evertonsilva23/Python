# Exercício 3: Reescreva o código guardião nos exemplos acima sem duas
# declarações if. Em vez disso, use uma expressão lógica composta usando
# o operador lógico or, com uma única declaração if.


# fhand = open('mbox-short.txt')
# contador = 0
# for line in fhand:
#     palavras = line.split()
# # print 'Debug:', palavras
#     if len(palavras) == 0 : continue
#     if palavras[0] != 'From' : continue
#     print(palavras[2])


fhand = open('mbox-short.txt')
contador = 0
for line in fhand:
    palavras = line.split()
    if len(palavras) == 0 or palavras[0] != 'From' : continue
    print(palavras[2])