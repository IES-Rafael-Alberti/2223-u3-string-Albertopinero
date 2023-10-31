'''Escribe un bucle while que comience con el último carácter en la cadena y 
haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente'''
def CadenaHaciaAtras():
    while palabra:
        for i in range(len(palabra)-1, -1, -1):
            return i
        return palabra
    
if __name__ == "__main__":
    #entrada
    palabra = input("Escribe una palabra: ")
    #proceso
    while palabra:
        for i in range(len(palabra)-1, -1, -1):
    #salida
            print(palabra[i])
        break