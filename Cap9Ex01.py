# Escreva um programa que leia as palavras em words.txt e as armazena
# como chaves em um dicionário. Não importa quais são os valores. Então,
# você pode usar o operador in como uma maneira rápida de verificar se
# uma string está no dicionário.

dictionary = dict()
fhand = open('words.txt')
for line in fhand:
    line = line.split()
    print(line)
    for word in line:
        dictionary[word] = ''
print(dictionary)
print('Our' in dictionary)