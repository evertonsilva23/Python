# fhand = open('mbox-short.txt')
# contador = 0
# for linha in fhand:
# palavras = line.split()
# # print 'Debug:', palavras
# if len(palavras) == 0 : continue
# if palavras[0] != 'De' : continue
# print(palavras[2])
# Primeiro, comentamos as linhas que imprimem o debug, em vez de removê-las
# (caso nossa modificação falhe, e precisemos do debuggingz novamente). Depois, adicionamos uma declaração guardiã que checa se temos zero palavras,
# se sim, nós usamos “continue” para pular para próxima linha do arquivo.
# Podemos pensar nas duas declarações continue como um jeito de nos ajudar
# a refinar o conjunto de linhas que são interessantes para nós, e quais que
# queremos processar um pouco mais. Uma linha que não tem “De” como sua
# primeira palavra não é interessante para nós, então a pulamos.
# O programa modificado é executado com sucesso, então, talvez ele esteja correto. Nossa declaração guardiã nos dá a certeza que a palavras[0] nunca irá
# falhar, porém, talvez isso não seja suficiente. Quando estamos programando,
# nós devemos sempre estar pensando, “O que pode acontecer de errado?”
# Exercício 2: Descubra qual linha do programa acima não está devidamente protegida. Veja se você pode construir um arquivo de texto que
# causa falha no programa e depois modifique o programa para que a
# linha seja propriamente protegida e por fim, teste o programa para ter
# certeza que ele manipula corretamente o novo arquivo de texto.


fhand = open('mbox-short2.txt')
contador = 0
for line in fhand:
    palavras = line.split()
    if len(palavras) == 0 : continue
    if palavras[0] != 'From' : continue
    print(palavras[2])

# Nesse caso nao consegui localizar uma falha onde pode gerar um erro no script.
