# Reto
# Devolver el resultado de la multiplicacion
# siempre y cuando no devuelva un valor maximo.

# Si vmax 50, mult = 102, retornar 50
# Si cmx 50, mul = 40, retornar 40

def operarConPares(operacion):
    def wrapper(*args, **kwargs):
        onlyEvenNumbers = list(filter(lambda num: num%2 == 0, args))
        resultado = operacion(*onlyEvenNumbers, **kwargs)
        print(f'El resultado de la operacion es: {resultado}')
        return resultado
    return wrapper



@operarConPares
def multiplicar(*args, **kwargs):
    
    
    acc = 1
    for num in args:
        acc *= num
    if 'max' in kwargs.keys():
        return min(kwargs['max'],acc)
    return acc

multiplicar(1,4,7,24,7,4,7, max = 200)
