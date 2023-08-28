# Exercício 4: Adicione linhas de código no programa abaixo para identificar quem possui mais mensagens no arquivo. Após todo o dado ser
# lido e todo o dicionário ser criado, procure no dicionário, utilizando um
# laço máximo (Veja o capítulo 5: Laços máximo e mínimo), quem tem o
# maior número de mensagens e mostre em tela quantas mensagens essa
# pessoa tem.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    if len(line) == 0 or not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    word = words[1]
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
largest = None
minimum = None
#Encontrando o maior valor no dicionário
for i in counts.values():
    if largest is None or i > largest:
        largest = i
    if minimum is None or i < minimum:
        minimum = i
#Localizando o valor e retornando a chave
def search_value(value):
    for k, v in counts.items():
        if value == v:
            return k
print(search_value(largest), largest)
print(search_value(minimum), minimum)
