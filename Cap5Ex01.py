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

# -*- encoding: utf-8 -*-
# coding: iso-8859-1 -*-
number = ""
i = 0
soma = 0
while number != "pronto":
    number = input("Digite um numero: ")
    if number != "pronto":
        try:
            xnumber = int(number)
            soma = soma + xnumber
            i = i + 1
        except:
            print("Dado invalido")
            continue

print("A soma total e: ", soma)
print("A quantidade de numeros e: ", i)
print("A media dos numeros e: ", soma / i)
