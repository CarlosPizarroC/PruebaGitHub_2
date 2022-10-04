# Este archivo es para crear clases

from random import randint, random


class carro:
    
    def __init__(self, nombre_del_carro: str) -> None:
        self.nombre: str = nombre_del_carro
        self.velocidad: int = randint(100, 250)
        print("Se creado el vehículo ", self.nombre, " con una velocidad de ", self.velocidad, "Km/h.")

    def andar(self, tiempo: int=None) -> None:
        if not tiempo:
            tiempo = randint(1, 10)

        for i in range(tiempo):
            print("El vehículo ", self.nombre, " ha recorrido ", self.velocidad*tiempo, "Km/h.")
            