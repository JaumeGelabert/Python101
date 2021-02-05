# En este script, lo que hacemos es comprobar si el usuario es capaz de introducir usuario y contrasena
# desde dos documentos externos diferentes. Hay dos usuarios y contrasenas.
# Usamos un for loop.

with open('a.txt') as usuarios:
    user = usuarios.readlines()

with open('b.txt') as contras:
    password = contras.readlines()

print("----------")
for i in range(len(user)):
    print(user[i]),
print("----------")
for i in range(len(password)):
    print(password[i]),
print("----------")

usuar = raw_input("Usuario: ")
passw = raw_input("Contrasena: ")

for i in range(len(user)):
    if(usuar == user[i].strip() and passw == password[i].strip()):
        print("ACCESO CORRECTO!"),