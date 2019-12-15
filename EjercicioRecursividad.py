import random, sys

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
