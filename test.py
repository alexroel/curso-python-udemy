def factorial(n:int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
resultado = factorial('5')
print("El factorial de 5 es:", resultado)  # Imprime: El factorial de 5 es: 120