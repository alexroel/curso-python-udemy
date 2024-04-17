class Animal:
    """Clase para representar un animal."""
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"


class Mascota(Animal):
    """Clase para representar una mascota, hereda de la clase Animal."""
    def __init__(self, nombre, especie, edad) -> None:
        super().__init__(especie, edad)
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Mascota: [Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"


class RegistroMascotas:
    """Clase para representar un registro de mascotas."""
    def __init__(self) -> None:
        self.mascotas = []

    def agregar_mascotas(self, mascota):
        """
        Agrega una mascota al registro.

        Parameters:
            mascota (Mascota): La mascota a agregar al registro.
        """
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        """
        Lista todas las mascotas registradas.
        """
        if self.mascotas:
            print("  Lista de mascotas \n", "="*30)
            for i, mascota in enumerate(self.mascotas, start=1):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas registradas.")

    def editar_mascota(self, indice, nuevo_mascota):
        """
        Edita una mascota en el registro.

        Parameters:
            indice (int): El índice de la mascota a editar.
            nuevo_mascota (Mascota): La nueva información de la mascota.
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            self.mascotas[indice] = nuevo_mascota
            print("Mascota editada correctamente.")

    def eliminar_mascota(self, indice):
        """
        Elimina una mascota del registro.

        Parameters:
            indice (int): El índice de la mascota a eliminar.
        """
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            del self.mascotas[indice]
            print("Mascota eliminada correctamente.")
