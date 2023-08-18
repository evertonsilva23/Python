# Exercício 2: Escreva um programa que solicite um arquivo e então leia
# ele e procure por linhas da forma:
# X-DSPAM-Confidence: 0.8475
# Quando encontrar uma linha que inicie com “X-DSPAM-Confidence:”
# separe a linha do texto para extrair o número de ponto flutuante que
# ela contém. Conte essas linhas e então compute o total de valores de
# Confiança de Spam nelas. Quando chegar no fim do arquivo, mostre a
# média de Confiança de Spam.
# Digite o nome de um arquivo: mbox.txt
# Média de confiança de spam: 0.894128046745
# Digite o nome de um arquivo: mbox-short.txt
# Média de confiança de spam: 0.750718518519
# Teste seu programa com os arquivos mbox.txt e mbox-short.txt
fname = input('Digite o nome de um arquivo: ')
try:
    fhand = open(fname)
except:
    fhand = open('mbox-short.txt')
    total = 0.0
    count = 0
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            fline = float(line[20:].rstrip('\n'))
            total = total + fline
            count += 1
print('Media de confianca de Spam: ', total / count)
        
        
