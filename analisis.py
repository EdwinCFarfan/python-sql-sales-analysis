import csv

ventas_totales = 0
productos = {}
clientes = {}

with open("ventas.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:

        cliente = fila["cliente"]
        producto = fila["producto"]
        cantidad = int(fila["cantidad"])
        precio = float(fila["precio"])

        total = cantidad * precio

        ventas_totales += total

        if producto in productos:
            productos[producto] += cantidad
        else:
            productos[producto] = cantidad

        if cliente in clientes:
            clientes[cliente] += total
        else:
            clientes[cliente] = total

print("VENTAS TOTALES")
print(f"${ventas_totales:.2f}")

print("\nPRODUCTOS MÁS VENDIDOS")

for producto, cantidad in sorted(productos.items(), key=lambda x: x[1], reverse=True):
    print(producto, cantidad)

print("\nGASTO POR CLIENTE")

for cliente, gasto in sorted(clientes.items(), key=lambda x: x[1], reverse=True):
    print(cliente, gasto)

cliente_top = max(clientes, key=clientes.get)

print("\nCLIENTE CON MAYOR GASTO")
print(cliente_top, clientes[cliente_top])