'''Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.'''
def cuenta():
    for i in frase:
        if i == letra:
            return i
        return i

if __name__ == "__main__":
    #entrada
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    #proceso
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    #salida
    print("La letra %s aparece %2i veces en la frase %s." % (letra, contador, frase))