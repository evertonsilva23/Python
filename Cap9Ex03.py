# Exercício 3: Escreva um programa que leia um registro de mensagens,
# construa um histograma, utilizando um dicionário, para contar quantas
# mensagens chegaram em cada endereço de email e mostre em tela o
# dicionário.
# Enter a file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    if len(line) == 0 or not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    # print(words)
    word = words[1]
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)