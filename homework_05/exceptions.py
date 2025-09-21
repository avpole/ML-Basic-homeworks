"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    """Ошибка: недостаточно топлива для запуска двигателя"""
    pass


class NotEnoughFuel(Exception):
    """Ошибка: недостаточно топлива для движения"""
    pass


class CargoOverload(Exception):
    """Ошибка: перегруз по грузу"""
    pass