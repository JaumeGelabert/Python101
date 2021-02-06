from random import seed
from random import randint

print("Adivina el numero...")
print("NORMAS:")
print("Entre 0 y 100, ambos incluidos.")
print("Numero entero, sin decimales.")
print("Solo tienes 5 intentos.")
print("-------------------")
rnd = randint(0,10) #Tambien hacemos random la seed. De esta manera cada vez que se compila, es un num
seed(rnd)
solucion = randint(0,100)
solucion_superior = solucion + randint(0,20)
solucion_inferior = solucion - randint(0,20)

guess = int(input("Primer intento: "))

if guess == solucion:
    print("HAS GANADO! La solucion es", solucion)
elif guess != solucion:
    print("ERROR 1.")
    print("PISTA 1: La solucion esta entre", solucion_inferior, solucion_superior, ", ambos incluidos." )

    guess2 = int(input("Segundo intento: "))
    if guess2 == solucion:
        print("HAS GANADO! La solucion es ", solucion)
    elif guess2 != solucion:
        print("ERROR 2.")
        if solucion%2 == 0:
            print("PISTA 2: La solucion es multiplo de dos, es decir, es PAR.")
        elif solucion%2 != 0:
            print("PISTA 2: La solucion NO es multiplo de dos, es decir, es IMPAR.")

        guess3 = int(input("Tercer intento: "))
        if guess3 == solucion:
            print("HAS GANADO! La solucion es ", solucion)
        elif guess3 != solucion:
            print("ERROR 3.")
            if guess3 > solucion:
                print("PISTA 3: La solucion es MENOR a tu intento. Recuerda que tu ultimo intento a sido el", guess3)
            elif guess3 < solucion:
                print("PISTA 3: La solucion es MAYOR a tu intento. Recuerda que tu ultimo intento a sido el", guess3)

            guess4 = int(input("Cuerto intento: "))
            solucion_superior_easy = solucion + randint(0,10)
            solucion_inferior_easy = solucion - randint(0,10)
            if guess4 == solucion:
                print("HAS GANADO! La solucion es ", solucion)
            elif guess4 != solucion:
                print("ERROR 4.")
                print("PISTA 4: La solucion esta entre ", solucion_inferior_easy, solucion_superior_easy, ", ambos incluidos.")
                print("Recuerda tus pistas anteriores!") #Estaria bien mostrar todas las pistas

            #Hacer que los numeros que se suman sean random, ya que si no siempre sera el del centro. 
            #Hacer que los numeros se ordenen de manera aleatoria
            lista_soluciones = [solucion, solucion+1, solucion+2, solucion-1, solucion-2]
            print(lista_soluciones) #Hacer que la lista se muestre en orden aleatorio. 
            guess5 = int(input("Quinto y ultimo intento. Elige entre uno de los numeros anteriores: "))
            if guess5 == solucion:
                print("HAS GANADO! La solucion es ", solucion)
            elif guess5 != solucion:
                print("HAS PERDIDO! La solucion es ", solucion)
            print("GRACIAS POR JUGAR!")
