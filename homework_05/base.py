from abc import ABC
from homework_05 import exceptions


class Vehicle:
    weight: int = 0
    started: bool = False
    fuel: int = 0
    fuel_consumption: int = 1

    def __init__(self, weight=0, fuel=0, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError("Нельзя завести: нет топлива")

    def move(self, distance: int):
        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
        else:
            raise exceptions.NotEnoughFuel(
                f"Недостаточно топлива для преодоления {distance} км"
            )
