#Exercício 3: Escreva um programa que peça por uma pontuação entre
#0.0 e 1.0. Se a pontuação for fora do intervalo, mostre uma mensagem
#de erro. Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota
#usando a seguinte tabela
#Pontuação Nota
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Digite a Pontuação: 0.95
#A
#Digite a Pontuação: perfeito
#Pontuação Inválida
#Digite a Pontuação: 10.0
#Pontuação Inválida
#Digite a Pontuação: 0.75
#C
#Digite a Pontuação: 0.5
#F
#Rode o programa repetidamente como mostrado acima para testar diferentes valores de entrada

try:
    pontuation = input("Digite a pontuação: ")
    fPontuation = float(pontuation)

except:
    print("Pontuação Inválida")
    quit()
    
if fPontuation >= 0.9 and fPontuation < 1.0:
    print("#A")
elif fPontuation >= 0.8 and fPontuation < 1.0:
    print("#B")
elif fPontuation >= 0.7 and fPontuation < 1.0:
    print("#C")
elif fPontuation >= 0.6 and fPontuation < 1.0:
    print("#D")
elif fPontuation < 0.6 and fPontuation > 0.0:
    print("#F")
else:
    print("Pontuação inválida")
    