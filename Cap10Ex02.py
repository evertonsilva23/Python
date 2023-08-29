# Exercício 2: Esse programa conta a distribuição de horas no dia para
# cada uma das mensagens. Você pode retirar a hora da linha com “From”
# achando a string de horário e então separando ela em partes usando o
# caractere “:” (dois pontos). Uma vez acumuladas as contagens para
# cada hora, mostre os valores, um por linha, ordenados por hora como
# segue abaixo:
# python timeofday.py
# Digite o nome do arquivo: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    if len(line) == 0 or not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    hour = words[5]
    print(hour)
