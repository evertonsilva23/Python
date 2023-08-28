# Exercício 5: Esse programa grava o domínio de email (ao invés do endereço) de onde a mensagem foi enviada ao invés de quem o email veio (
# i.e., o endereço completo da mensagem). No final do programa, mostre
# em tela o conteúdo do seu dicionário.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


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
print(counts) #Imprime o dicionário contendo os domínios e quantas vezes ele aparece no arquivo