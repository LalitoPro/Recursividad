import random, sys
class dos_tres_cinco:
    __multiplosDos = 0
    __multiplosTres = 0
    __multiplosCinco =  0

# metodo donde se resive el nuemero a evaluar
    def condicion(self,numero):
        # pasamos a cadema de testo el numero
        a =str(numero)
        # se agreaga a una lista
        A = list(a)
        #iniciamos el recorrido del la cadena de texto desde la ultia posicion.
        for i in range(-1, (len(A) + 1) * -1, -1):
            # se avalua si son porsentuales de 2
            if abs(i) % 2 == 0:
                # si cumplen con la condicion se van acomulando en un contador
                self.__multiplosDos += int(A[i])
            # se avalua si son porsentuales de 3
            if abs(i) % 3 == 0:
                self.__multiplosTres += int(A[i])
            # se avalua si son porsentuales de 5
            if abs(i) % 5 == 0:
                self.__multiplosCinco += int(A[i])
        if (self.__multiplosDos == self.__multiplosTres + self.__multiplosCinco):
            print(a, " es un numeero dos tres cinco")
        else:
            print(a, "no es un numero dos tres cinco")

def main():

    prueba = dos_tres_cinco()
    prueba.condicion(56321)


if __name__ == "__main__":
    main()



"""
codico estructurado
a= str(56321)
A = list(a)

multiplosDos = 0
multiplosTres = 0
multiplosCinco = 0
for i in range(-1, (len(A) + 1)*-1, -1):
    if abs(i) % 2 == 0:
        multiplosDos += int(A[i])
    if abs(i) % 3 == 0:
        multiplosTres += int(A[i])
    if abs(i) % 5 == 0:
        multiplosCinco += int(A[i])

if(multiplosDos == multiplosTres + multiplosCinco):
    print(a, " es un numeero dos tres cinco")
else:
    print(a, "no es un numero dos tres cinco")
"""