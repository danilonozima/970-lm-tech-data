def soma(a, b): 
    if not(isinstance(a, (int, float))):
        if not(isinstance(b, (int, float))):
          raise TypeError(f"O input 'a' e 'b' devem números. Recebido 'a' = {a}, tipo {type(a)}. E 'b'= {b}, tipo {type(b)}")
        else: 
          raise TypeError(f"O input 'a' deve ser um número. Recebido 'a' = {a}, tipo {type(a)}.")
    elif not(isinstance(b, (int, float))):
        raise TypeError(f"O input 'b' deve ser um número. Recebido 'b' = {b}, tipo {type(b)}.")
    else:
        return a + b