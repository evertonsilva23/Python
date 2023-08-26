# Escreva um programa que categorize cada mensagem de
# e-mail de acordo com o dia em que a mensagem foi enviada. Para
# isso, procure por linhas que comecem com “From”, depois procure pela
# terceira palavra e mantenha uma contagem de ocorrência para cada dia
# da semana. No final do programa, mostre em tela o conteúdo do seu
# dicionário (a ordem não interessa).
# linha exemplo:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Exemplo de código:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Sex': 20, 'Qui': 6, 'Sab': 1}
# Exercício 3: Escreva um programa que leia um 

counts = dict()
fhand = open('mbox.txt')
for line in fhand:
    if len(line) == 0 or not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    # print(words)
    word = words[2]
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)