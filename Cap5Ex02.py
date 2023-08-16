# Exercício 1: Escreva um programa que lê repetitivamente números até
# que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a
# soma total, a quantidade e a média dos números digitados. Se o usuário
# digitar qualquer coisa que não seja um número, detecte o erro usando
# o trye o except e mostre na tela uma mensagem de erro e pule para o
# próximo número.
# Digite um número: 4
# Digite um número: 5
# Digite um número: dado errado
# Entrada Inválida
# Digite um número: 7
# Digite um número: pronto
# 16 3 5.333333333333333
# Exercício 2: Escreva outro programa que pede por uma lista de números
# como mostrada acima e mostra, no final, o máximo e o mínimo dos
# números ao invés da média.

number = ""
lista = []
while number != "pronto":
    number = input("Digite um numero: ")
    if number != "pronto":
        try:
            xnumber = int(number)
            lista.append(number)
        except:
            print("Dado invalido")
            continue

print("O menor numero e: ", min(lista))
print("O maior numero e: ", max(lista))
print(lista)