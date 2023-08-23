from cliente import Cliente

cliente1 = Cliente("López Renzo", 30, "renzo@gmail.com", "Calle Principal 123")
cliente2 = Cliente("Edgardo Juan", 25, "edgardo@hotmail.com", "Avenida Central 100")


print(cliente1)
print(cliente2)

cliente1.realizar_compra(100)

cliente2.actualizar_direccion("Calle actualizada 940")

print(cliente2)
