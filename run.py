from poo import Mascota, RegistroMascotas

registro = RegistroMascotas()



while True:
   menu = """--- Menú ---
1. Agregar mascota
2. Listar mascotas
3. Editar mascota
4. Eliminar mascota
5. Salir
Ingrese una opción: """

   opcion = input(menu)
   if opcion == "1":
      nombre = input("Nombre de la mascota: ")
      especie = input("Especie de la mascota: ")
      edad = input("Edad de la mascota: ")

      mascota = Mascota(nombre, especie, edad)
      registro.agregar_mascotas(mascota)

   elif opcion == "2":
      registro.listar_mascotas()
   
   elif opcion == "3":
      indice = int(input("Ingrese indice del registro: "))
      nombre = input("Nombre de la mascota: ")
      especie = input("Especie de la mascota: ")
      edad = input("Edad de la mascota: ")

      nueva_mascota = Mascota(nombre, especie, edad)
      registro.editar_mascota(indice-1, nueva_mascota)
   
   elif opcion == "4":
      indice = int(input("Ingrese el índice de la mascota a eliminar: "))
      registro.eliminar_mascota(indice - 1)

   elif opcion == "5":
      print("¡Hasta luego!")
      break
   else:
      print("Opción inválida. Por favor, elija una opción válida.")
      