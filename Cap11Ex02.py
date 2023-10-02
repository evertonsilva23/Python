
# Exercício 2: Escreva um programa que procure por uma linha na forma:
# Nova Revisão: 39772
# New Revision: 39772
# Extraia o número de cada linha usando uma expressão regular e o
# método findall(). Compute o valor médio dos números e mostre-o.
# Arquivo de entrada: mbox.txt
# 38444.0323119
# Arquivo de entrada: mbox-short.txt
# 39756.9259259

import re
count = list()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New \S*: ([0-9.]+)', line)
    if len(x) > 0:
        count.append(float(x[0]))
print(sum(count) / len(count))