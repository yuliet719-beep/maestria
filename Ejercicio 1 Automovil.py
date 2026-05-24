"""
Patron: Builder (Creacional)
Construccion de objetos Car con configuraciones relacionadas.
"""

from dataclasses import dataclass

@dataclass
class Automovil:
    motor: str = "Motor estandar"
    color: str = "Blanco"
    llantas: str = "Llantas estandar"
    sistema_sonido: str = "Radio basica"
    interiores: str = "Interiores de tela"
    techo_solar: bool = False
    navegacion_gps: bool = False

    def __str__(self) -> str:
        return (
            f"Car: motor={self.motor}, "
            f"color={self.color}, "
            f"llantas={self.llantas}, "
            f"sistema_sonido={self.sistema_sonido}, "
            f"interiores={self.interiores}, "
            f"techo_solar={'Si' if self.techo_solar else 'No'}, "
            f"navegacion_gps={'Si' if self.navegacion_gps else 'No'}"
        )


class Builder:
    def reset(self) -> None:
        raise NotImplementedError

    def set_motor(self, motor: str) -> None:
        raise NotImplementedError

    def set_color(self, color: str) -> None:
        raise NotImplementedError

    def set_llantas(self, llantas: str) -> None:
        raise NotImplementedError

    def set_sistema_sonido(self, sistema_sonido: str) -> None:
        raise NotImplementedError

    def set_interiores(self, interiores: str) -> None:
        raise NotImplementedError

    def set_techo_solar(self, enabled: bool) -> None:
        raise NotImplementedError

    def set_navegacion_gps(self, enabled: bool) -> None:
        raise NotImplementedError

    def get_product(self):
        raise NotImplementedError


class AutomovilBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._automovil = Automovil()

    def set_motor(self, motor: str) -> None:
        self._automovil.motor = motor

    def set_color(self, color: str) -> None:
        self._automovil.color = color

    def set_llantas(self, llantas: str) -> None:
        self._automovil.llantas = llantas

    def set_sistema_sonido(self, sistema_sonido: str) -> None:
        self._automovil.sistema_sonido = sistema_sonido

    def set_interiores(self, interiores: str) -> None:
        self._automovil.interiores = interiores

    def set_techo_solar(self, enabled: bool) -> None:
        self._automovil.techo_solar = enabled

    def set_navegacion_gps(self, enabled: bool) -> None:
        self._automovil.navegacion_gps = enabled

    def get_product(self) -> Automovil:
        product = self._automovil
        self.reset()
        return product


class Director:
    def construct_sports_car(self, builder: Builder) -> None:
        builder.reset()
        builder.set_motor("Motor V8")
        builder.set_color("Rojo metalico")
        builder.set_llantas("Llantas deportivas 20\"")
        builder.set_sistema_sonido("Equipo premium")
        builder.set_interiores("Cuero negro")
        builder.set_techo_solar(True)
        builder.set_navegacion_gps(True)

    def construct_luxury_car(self, builder: Builder) -> None:
        builder.reset()
        builder.set_motor("Motor V6 Turbo")
        builder.set_color("Azul oscuro")
        builder.set_llantas("Llantas aleacion 19\"")
        builder.set_sistema_sonido("Sistema Bose")
        builder.set_interiores("Cuero beige")
        builder.set_techo_solar(True)
        builder.set_navegacion_gps(True)


def main() -> None:
    director = Director()

    automovil_builder = AutomovilBuilder()
    default_automovil = automovil_builder.get_product()

    director.construct_sports_car(automovil_builder)
    deportivo_automovil = automovil_builder.get_product()

    director.construct_luxury_car(automovil_builder)
    lujoso_automovil = automovil_builder.get_product()

    print("Auto por defecto:")
    print(default_automovil)
    print()
    print("Auto deportivo:")
    print(deportivo_automovil)
    print()
    print("Auto de lujo:")
    print(lujoso_automovil)


if __name__ == "__main__":
    main()

"""
SALIDA ESPERADA
Auto por defecto:
Car: motor=Motor estandar, color=Blanco, llantas=Llantas estandar, sistema_sonido=Radio basica, interiores=Interiores de tela, techo_solar=No, navegacion_gps=No

Auto deportivo:
Car: motor=Motor V8, color=Rojo metalico, llantas=Llantas deportivas 20", sistema_sonido=Equipo premium, interiores=Cuero negro, techo_solar=Si, navegacion_gps=Si

Auto de lujo:
Car: motor=Motor V6 Turbo, color=Azul oscuro, llantas=Llantas aleacion 19", sistema_sonido=Sistema Bose, interiores=Cuero beige, techo_solar=Si, navegacion_gps=Si
"""
