def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def restar(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def dividir(numero1, numero2):
    if (numero2 == 0):
        print("no se divide para cero")
        return
    resultado = numero1 / numero2
    return resultado