# Exercicio 4: Baixe a copia do arquivo www.py4e.com/code3/romeo.txt.
# Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por
# linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
# Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
# adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
# palavras em ordem alfabética.**
# Digite o nome do arquivo: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']



wordlist = [] #Criando uma lista vazia
fhand = open('romeo.txt') #Abrindo o arquivo e guardando o conteudo na variavel fhand
for line in fhand : #Criando um loop para passar linha a linha e dividir a linha em uma lista de palavras
    sline = line.split()
    for word in sline:  #Criando um loop para passar palavra a palavra em cada linha do arquivo
        if word not in wordlist: #Verificando se a palavra nao esta na lista de palavras
            wordlist.append(word) #Adicionando as palavras que passaram na verificacao a lista
wordlist.sort() #Colocando a lista em ordem para imprimir
print(wordlist)

