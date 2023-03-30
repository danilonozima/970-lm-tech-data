from funcoes import soma, subtracao, divisao, multiplicacao

def calcule(): 
    a = input('Inpute um número a: ')
    b = input('Inpute um número b: ')
    try: 
        a = int(a)
    except:
        try:
            a = float(a)
        except: 
            pass
    try:
        b = int(b)
    except:
        try:
            b = float(b)
        except:
            pass
    operacao = input('Digite a operação desejada: soma (+), subtração (-), divisão (/) our multiplicação (*): ')
    if operacao == 'soma' or operacao == '+':
        return soma(a, b)
    elif operacao == 'subtração' or operacao == '-':
        return subtracao(a, b)
    elif operacao == 'divisão' or operacao == '/':
        return divisao(a, b)
    elif operacao == 'multiplicação' or operacao == '*':
        return multiplicacao(a, b)