# Exercício 1: Revise um programa anterior como é pedido: Leia e analise
# as linhas com “From” e retire os endereços dessas linhas. Conte o
# número de mensagens de cada pessoa usando um dicionário. Depois de
# todos os dados serem lidos, mostre a pessoa com mais envios criando
# uma lista de tuplas (contagem, email) do dicionário. Então, ordene a
# lista em ordem reversa e mostre a pessoa na primeira posição.
# Linha simples:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Digite o nome do arquivo: mbox-short.txt
# cwen@iupui.edu 5
# Digite o nome do arquivo: mbox.txt
# zqian@umich.edu 195


counts = dict()
fhand = open('mbox-short.txt')
#Loop para quebrar o arquivo em linhas
for line in fhand:
    if len(line) == 0 or not line.startswith('From '): continue #Verifica se a linha é vazia ou se não inicia com 'From'
    line = line.rstrip() #Retira as quebras de linhas do arquivo
    words = line.split() #Divida a linha em palavras
    mail = words[1] #Armazena o e-mail completo na variável
    pos = mail.find('@') #localiza a posição do char @
    domain = mail[pos + 1:] #Armazena o restante do e-mail após a @, que seria o domínio
    if domain not in counts: #Verifica se o domínio não existe no dicionário, se não existe adiciona ele com o valor 1
         counts[domain] = 1
    else:
        counts[domain] += 1 #Se o domínio já existe complementa o valor dele em 1
# print(counts) #Imprime o dicionário contendo os domínios e quantas vezes ele aparece no arquivo
lst = list()
for key, val in list(counts.items()):
   lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:1]:
    print(key, val)