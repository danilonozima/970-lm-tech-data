def soma(a, b): 
    if not(isinstance(a, (int, float))):
        if not(isinstance(b, (int, float))):
          raise TypeError(f"O input 'a' e 'b' devem ser números. Recebido 'a' = {a}, tipo {type(a)}. E 'b'= {b}, tipo {type(b)}")
        else: 
          raise TypeError(f"O input 'a' deve ser um número. Recebido 'a' = {a}, tipo {type(a)}.")
    elif not(isinstance(b, (int, float))):
        raise TypeError(f"O input 'b' deve ser um número. Recebido 'b' = {b}, tipo {type(b)}.")
    else:
        return a + b
    
def subtracao (a, b): 
    if not(isinstance(a, (int, float))):
        if not(isinstance(b, (int, float))):
          raise TypeError(f"O input 'a' e 'b' devem ser números. Recebido 'a' = {a}, tipo {type(a)}. E 'b'= {b}, tipo {type(b)}")
        else: 
          raise TypeError(f"O input 'a' deve ser um número. Recebido 'a' = {a}, tipo {type(a)}.")
    elif not(isinstance(b, (int, float))):
        raise TypeError(f"O input 'b' deve ser um número. Recebido 'b' = {b}, tipo {type(b)}.")
    else:
        return a - b

def divisao (a, b): 
    if not(isinstance(a, (int, float))):
        if not(isinstance(b, (int, float))):
          raise TypeError(f"O input 'a' e 'b' devem ser números. Recebido 'a' = {a}, tipo {type(a)}. E 'b'= {b}, tipo {type(b)}")
        else: 
          raise TypeError(f"O input 'a' deve ser um número. Recebido 'a' = {a}, tipo {type(a)}.")
    elif not(isinstance(b, (int, float))):
        raise TypeError(f"O input 'b' deve ser um número. Recebido 'b' = {b}, tipo {type(b)}.")
    elif b == 0:
        raise ZeroDivisionError('Divisão por zero')
    else: 
        return a / b