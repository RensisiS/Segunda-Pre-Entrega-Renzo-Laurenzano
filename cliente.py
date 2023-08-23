# cliente.py

class Cliente:
    def __init__(self, nombre, edad, email, direccion):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.direccion = direccion

    def realizar_compra(self, monto):
        # Aquí podrías agregar la lógica para realizar la compra
        print(f"{self.nombre} ha realizado una compra por ${monto}")

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def __str__(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}, Email: {self.email}, Dirección: {self.direccion}"