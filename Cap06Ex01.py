# Exercício 1: Escreva um loop while que inicia no último caractere da
# string e caminha para o primeiro caractere, imprimindo cada letra em
# uma linha separada.
# Outra forma de escrever uma travessia é com um laço for:
# for char in fruta:
# print(char)
# Cada vez que passa pelo laço, o próximo caractere da string é atribuído à variável
# char. O laço continua até o fim dos caracteres.

palavra = input("Digite uma palavra: ")
tamanho = len(palavra)
while tamanho > 0:
    print(palavra[tamanho - 1])
    tamanho -= 1
    
for char in palavra:
    print(char)