# Solicitar al usuario que ingrese el monto de consumo
total_amount = float(input("Ingrese el monto de consumo: $"))

# Calcular el descuento
if total_amount > 50 and total_amount <= 100:
    discount_percentage = 0.1
elif total_amount > 100 and total_amount <= 200:
    discount_percentage = 0.2
elif total_amount > 200:
    discount_percentage = 0.3
else:
    discount_percentage = 0.0

# Calcular el monto final con descuento
discount_amount = total_amount * discount_percentage
final_amount = total_amount - discount_amount

# Mostrar el resumen de la cuenta en español
print("\nResumen de la cuenta:")
print(f"Monto de consumo: ${total_amount:.2f}")
print(f"Descuento aplicado: {discount_percentage * 100:.0f}%")
print(f"Monto final con descuento: ${final_amount:.2f}")