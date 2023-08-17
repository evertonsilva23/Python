# Exercício 5: Utilize o seguinte código em Python que guarda uma string:
# str = 'X-DSPAM-Confidence:0.8475' Use a função find e o fatiamento de
# strings para extrair a porção da string depois do sinal de dois pontos e
# use a função float para converter a string extraída em um número de
# ponto flutuante.


str = 'X-DSPAM-Confidence:0.8475'

#Localizando a posicao dos caracteres solicitado.
pos = str.find(':')
print(pos)

#Guardando o pedaco da string em uma variavel
number = str[19:]
print(number)

#Convertendo a string em um ponto flutuante
fNumber = float(number)
print(fNumber, type(fNumber))