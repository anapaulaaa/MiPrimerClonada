class vivienda:
    def __init__(self, ventanas, puertas, techo, color):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.color = color

    def get_ventanas(self):
        return self.ventanas

    def get_puertas(self):
        return self.puertas

    def get_techo(self):
        return self.techo

    def get_color(self):
        return self.color

    def set_ventanas(self, ventanas):
        self.ventanas = ventanas

    def set_puertas(self, puertas):
        self.puertas = puertas

    def set_techo(self, techo):
        self.techo = techo

    def set_color(self, color):
        self.color = color

    def mostrar_info(self):
        print(f"Ventanas: {self.ventanas}")
        print(f"Puertas: {self.puertas}")
        print(f"Techo: {self.techo}")
        print(f"Color: {self.color}")


class ViviendaFamiliar(vivienda):
    def __init__(self, ventanas, puertas, techo, color, habitaciones):
        vivienda.__init__(self, ventanas, puertas, techo, color)
        self.habitaciones = habitaciones

    def get_habitaciones(self):
        return self.habitaciones

    def set_habitaciones(self, habitaciones):
        self.habitaciones = habitaciones

    def mostrar_info(self):
        vivienda.mostrar_info(self)
        print(f"Habitaciones: {self.habitaciones}")


class Apartamento(vivienda):
    def __init__(self, ventanas, puertas, techo, color, piso):
        vivienda.__init__(self, ventanas, puertas, techo, color)
        self.piso = piso

    def get_piso(self):
        return self.piso

    def set_piso(self, piso):
        self.piso = piso

    def mostrar_info(self):
        vivienda.mostrar_info(self)
        print(f"Piso: {self.piso}")


vf = ViviendaFamiliar(6, 2, "Teja", "Blanca", 4)
vf.mostrar_info()

print()

ap = Apartamento(4, 1, "Concreto", "Gris", 5)
ap.mostrar_info()
