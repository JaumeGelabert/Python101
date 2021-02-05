# En este script, lo que hacemos es comprobar si el usuario es capaz de introducir dos contraseñas 
# guardadas en un documento externo en un orden determinado.

with open('a.txt') as documento:
    palabras = documento.readlines()

for i in range(len(palabras)):
    print(palabras[i]),

c1 = raw_input("Contrasena 1: ")

if c1 == palabras[0].strip():
    print("Primera contrasena correcta.")
    c2 = raw_input("Contrasena 2: ")
    if c2 == palabras[1].strip():
        print("Ambas contrasenas correctas. ACCESO VALIDO")

        # AQUI CORRERIA EL CODIGO UNA VEZ EL USUARIO SE A IDENTIFICADO CORRECTAMENTE #

else:
    print("Contrasena 1 INCORRECTA. ")