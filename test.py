# # Solicitar al usuario que ingrese una palabra
# palabra = input("Ingrese una palabra: ")

# # convertirla a minúsculas)
# palabra = palabra.lower()

# #eliminar espacios
# palabra = palabra.replace(" ", "")

# # Invertir palabra
# palabra_invertida = palabra == palabra[::-1]

# # Mostrar el resultado al usuario
# if palabra == palabra_invertida:
#     print(f"{palabra} es un palíndromo.")
# else:
#     print(f"{palabra} no es un palíndromo.")


# Solicita al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Convierte la palabra a minúsculas y elimina espacios en blanco
palabra = palabra.lower().replace(" ", "")

# Muestra el resultado
print("Es un palíndromo." if palabra == palabra[::-1] else "No es un palíndromo.")