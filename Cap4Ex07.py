# Exercício 7: Reescreva o programa de notas do capítulo anterior usando a função computarNotas que recebe a pontuação como parâmetro e
# retorna a nota como uma string.
# Pontuação Nota
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Insira a pontuação: 0.95
# A
# Insira a pontuação: perfeito
# Pontuação Inválida
# Insira a pontuação: 10.0
# Pontuação Inválida
# Insira a pontuação: 0.75
# C
# Insira a pontuação: 0.5
# F
# Execute o programa repetitivamente para testar vários valores diferentes como
# entrada.

def computarNotas(pontuation):
    try:
        pontuation = input("Digite a pontuação: ")
        fPontuation = float(pontuation)

    except:
        print("Pontuação Inválida")
        quit()
    nota = ''
    if fPontuation >= 0.9 and fPontuation < 1.0:
        nota = "#A"
    elif fPontuation >= 0.8 and fPontuation < 1.0:
        nota = "#B"
    elif fPontuation >= 0.7 and fPontuation < 1.0:
        nota = "#C"
    elif fPontuation >= 0.6 and fPontuation < 1.0:
        nota = "#D"
    elif fPontuation < 0.6 and fPontuation > 0.0:
        nota = "#F"
    else:
        nota = "Pontuação inválida"
    return(nota)
nota = computarNotas(0.75)
print(nota)