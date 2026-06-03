import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("ventas.db")

# Crear cursor
cursor = conexion.cursor()

# Consulta 1: Total gastado por cliente
consulta_clientes = """
SELECT
    c.nombre,
    SUM(pr.precio * dp.cantidad) AS total_gastado
FROM clientes c
JOIN pedidos p
    ON c.id = p.cliente_id
JOIN Detalle_Pedidos dp
    ON p.id = dp.pedido_id
JOIN productos pr
    ON dp.producto_id = pr.id
GROUP BY c.nombre
ORDER BY total_gastado DESC;
"""

cursor.execute(consulta_clientes)
clientes = cursor.fetchall()

print("=" * 40)
print("CLIENTES CON MAYOR GASTO")
print("=" * 40)

for nombre, gasto in clientes:
    print(f"{nombre}: ${gasto:.2f}")

# Consulta 2: Productos más vendidos
consulta_productos = """
SELECT
    pr.nombre,
    SUM(dp.cantidad) AS unidades_vendidas
FROM productos pr
JOIN Detalle_Pedidos dp
    ON pr.id = dp.producto_id
GROUP BY pr.nombre
ORDER BY unidades_vendidas DESC;
"""

cursor.execute(consulta_productos)
productos = cursor.fetchall()

print("\n" + "=" * 40)
print("PRODUCTOS MÁS VENDIDOS")
print("=" * 40)

for producto, cantidad in productos:
    print(f"{producto}: {cantidad} unidades")

# Consulta 3: Cantidad de pedidos por cliente
consulta_pedidos = """
SELECT
    c.nombre,
    COUNT(p.id) AS cantidad_pedidos
FROM clientes c
JOIN pedidos p
    ON c.id = p.cliente_id
GROUP BY c.nombre
ORDER BY cantidad_pedidos DESC;
"""

cursor.execute(consulta_pedidos)
pedidos = cursor.fetchall()

print("\n" + "=" * 40)
print("CANTIDAD DE PEDIDOS POR CLIENTE")
print("=" * 40)

for cliente, cantidad in pedidos:
    print(f"{cliente}: {cantidad} pedido(s)")

# Consulta 4: Precio promedio de productos
consulta_promedio = """
SELECT AVG(precio)
FROM productos;
"""

cursor.execute(consulta_promedio)
promedio = cursor.fetchone()

print("\n" + "=" * 40)
print("PRECIO PROMEDIO DE PRODUCTOS")
print("=" * 40)

print(f"${promedio[0]:.2f}")

# Cerrar conexión
conexion.close()
