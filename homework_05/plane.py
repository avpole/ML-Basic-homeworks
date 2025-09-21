from homework_05.base import Vehicle
from homework_05 import exceptions


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight=0, fuel=0, fuel_consumption=1, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo: int):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise exceptions.CargoOverload(
                f"Перегруз! Текущий груз: {self.cargo}, добавляем: {cargo}, "
                f"максимум: {self.max_cargo}"
            )

    def remove_all_cargo(self) -> int:
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo