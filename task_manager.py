
class Animal:
   def __init__(self, especie, edad):
      self.__especie = especie
      self.__edad = edad

   def get_especie(self):
      return self.__especie
   
   def set_especie(self, especie):
      self.__especie = especie

   def __str__(self) -> str:
      return f"Animal[Especie: {self.__especie}, Edad: {self.__edad}]"
      

animal1 = Animal("Fido", "1 Año")
print(animal1.get_especie()) 