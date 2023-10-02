# Exercício 1: Escreva um programa simples para simular a operação do
# comando grep em Unix. Peça ao usuário para entrar com uma expressão
# regular e conte o número de linhas que se igualam à expressão digitada:
# $ python grep.py
# Digite uma expressão regular: ^Autor
# mbox.txt teve 1798 linhas que se igualam a ^Autor
# $ python grep.py
# Digite uma expressão regular: ^Xmbox.txt teve 14368 linhas que se igualam a ^X-
# $ python grep.py
# Digite uma expressão regular: java$
# mbox.txt teve 4175 linhas que se igualam a java$

import re
count = 0
hand = open('mbox.txt')
word = input('Digite uma expressao regular: ')
for line in hand:
    line = line.rstrip()
    x = re.search(word, line)
    if x:
        count +=1
print('mbox.txt teve', count, 'linhas que se igualam a', word)