# Exercício 6: Reescreva o programa que solicita o usuário uma lista de
# números e prints e imprime em tela o maior número e o menor número
# quando o usuário digitar a palavra “feito”. Escreva um programa para
# armazenar as entradas do usuário em uma lista e use as funções max()
# e min() para computar o número máximo e o mínimo depois que o laço
# for completo.
# Digite um número: 6
# Digite um número: 2
# Digite um número: 9
# Digite um número: 3
# Digite um número: 5
# Digite um número: feito
# Máximo: 9.0
# Mínimo: 2.0

number = 0
total = [] #Inicializando a lista vazia que vai receber os numeros inseridos.
while number != 'feito': #Testando a variavel de entrada que enquanto for diferente de feito, continua no laco
    number = input('Digite um numero: ') #Pedindo entrada para o usuario
    try: inumber = int(number) #Colocando uma protecao para caso seja digitado algo que nao seja um inteiro
    except:
        print('Digite um numero valido') #Mensagem de except para avisar o usuario do erro
        continue
    if type(inumber) == int: #Testando se a entrada e um inteiro ou nao para adicionar a lista
        total.append(inumber) #Adicionando a entrada na lista apos o teste
print('Maximo:', max(total)) #Imprimindo o maior numero
print('Minimo:', min(total)) #Imprimindo o menor numero
