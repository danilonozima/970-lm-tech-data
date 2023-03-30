from funcoes import soma, subtracao, divisao, multiplicacao

def calcule(): 
    a = input('Inpute um número a: ')
    b = input('Inpute um número b: ')
    operacao = input('Digite a operação desejada: soma (+), subtração (-), divisão (/) our multiplicação (*): ')
    if operacao == 'soma' or operacao == '+':
        soma(a, b)
    elif operacao == 'subtração' or operacao == '-':
        subtracao(a, b)
    elif operacao == 'divisão' or operacao == '/':
        divisao(a, b)
    elif operacao == 'multiplicação' or operacao == '*':
        multiplicacao(a, b)