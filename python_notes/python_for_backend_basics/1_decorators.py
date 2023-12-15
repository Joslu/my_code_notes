# Decorators
# Lo decoradores sirven para modificar
# el comportamiento de una función


print('###################################################### APARTADO 1 ###################################')
'''Apartado1: Las funciones sob objetos
Por lo tanto:
    - Es una instancia de tipo objeto
    - Podemos almacenar una función en una variable
    - Podemos pasar una función como parámetro de otra función
    - Una función puede retornar otra función
    - Se puede almacenar estructuras de datos, tablas, listas...
'''

def funcionExterna(nombre):
    
    def funcionEnvoltorio():
        print('Empieza la funcion envoltorio')
        print(nombre)
        print('Final de la funcion envoltorio')
        
    return funcionEnvoltorio


intancia_funcion = funcionExterna('Hola')
intancia_funcion()
print(type(intancia_funcion))


print('###################################################### APARTADO 2 ###################################')

'''Apartado 2: Funcion como argumento de otra función
En vez de pasar la valirable 'nombre', pasaremos otra función '''
 
from datetime import datetime

def getFecha():
    print(datetime.today().strftime("%d-%m-%Y"))
    
def getHora():
    print(datetime.now().strftime("%H:%M:%S"))
    
def funcionExterna(funcionInterna):
    def funcionEnvoltorio():
        print('Empieza la funcion envoltorio')
        funcionInterna()
        print('Fin funcion envoltorio')
    return funcionEnvoltorio

mostrarHora = funcionExterna(getHora)
mostrarFecha = funcionExterna(getFecha)

mostrarHora()
mostrarFecha()


print('###################################################### APARTADO 3 ###################################')
'''Apartado3: Sintaxis de los decoradores
'''

    
def funcionExterna2(funcionInterna):
    def funcionEnvoltorio():
        print('Empieza la funcion envoltorio')
        funcionInterna()
        print('Fin funcion envoltorio')
    return funcionEnvoltorio

@funcionExterna2
def saludar():
    print('Hola Crack')
    
@funcionExterna2
def depedirse():
    print('chauuuuuuuuuuuuuuu')

saludar()
depedirse()

print('###################################################### APARTADO 4 ###################################')

'''Apartado4: Funciones con argumentos
Veremos como podemo usar decoradores con funciones
que reciben diferenetes numeros de argumentos
'''


def sumarNuneros(*args, **kwargs):
    acc = 0
    for num in args:
        acc += num
    return acc


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
    return acc

multiplicar(1,4,7,24,7,4,7)