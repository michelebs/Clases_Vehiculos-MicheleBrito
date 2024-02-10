# Definición de la clase Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Definición de la clase Carro
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

# Definición de la clase Barco
class Barco(Vehiculo):
    def __init__(self, marca, modelo, eslora):
        super().__init__(marca, modelo)
        self.eslora = eslora

# Definición de la clase Avión
class Avion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros):
        super().__init__(marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros

# Inicialización de al menos dos objetos de cada tipo
carro1 = Carro("Toyota", "Corolla", "Rojo")
carro2 = Carro("Ford", "Mustang", "Negro")

barco1 = Barco("Yamaha", "Modelo X", 30)
barco2 = Barco("Mercury", "Modelo Y", 40)

avion1 = Avion("Boeing", "747", 416)
avion2 = Avion("Airbus", "A380", 555)

# Imprimir información de los vehículos
print("Carros:")
print(carro1.marca, carro1.modelo, carro1.color)
print(carro2.marca, carro2.modelo, carro2.color)

print("--------------------------------------------------------------")

print("Barcos:")
print(barco1.marca, barco1.modelo, barco1.eslora)
print(barco2.marca, barco2.modelo, barco2.eslora)

print("--------------------------------------------------------------")

print("Aviones:")
print(avion1.marca, avion1.modelo, avion1.capacidad_pasajeros)
print(avion2.marca, avion2.modelo, avion2.capacidad_pasajeros)
