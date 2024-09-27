#Python Fundamentals / Ejercicios Listas, Tuplas y diccionarios (Core) - Diego Amarilla

# 1. Carga de datos
ventas = [
    {'fecha': '2024-01-01', 'producto': 'Pan', 'cantidad': 10, 'precio': 5000},
    {'fecha': '2024-01-02', 'producto': 'Leche', 'cantidad': 5, 'precio': 7000},
    {'fecha': '2024-01-03', 'producto': 'Pan', 'cantidad': 3, 'precio': 5000},
    {'fecha': '2024-01-03', 'producto': 'Huevos', 'cantidad': 7, 'precio': 30000},
    {'fecha': '2024-01-04', 'producto': 'Leche', 'cantidad': 8, 'precio': 7000},
]

#2. Cálculo de Ingresos Totales

ingreso_total = 0
for venta in ventas:    
    ingreso_total += venta['cantidad'] * venta['precio']

print(f"Ingresos totales: Gs. {ingreso_total}")

#3. Análisis del producto más vendido

ventas_por_producto = {}
for venta in ventas:
    producto = venta['producto']
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta['cantidad']
    else:
        ventas_por_producto[producto] = venta['cantidad']

print(f"Producto mas vendido: {max(ventas_por_producto, key=ventas_por_producto.get)}")

#4. Promedio de Precio por Producto

precios_por_producto = {}
for venta in ventas:
    producto = venta['producto']
    cantidad = venta['cantidad']
    precio_total = venta['precio'] * cantidad
    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0]+ precio_total, 
            precios_por_producto[producto][1] + cantidad
        )
    else:
        precios_por_producto[producto] = (precio_total, cantidad)

precio_promedio_por_producto = {producto: total[0] / total[1] for producto, total in precios_por_producto.items()}

print(f"Precio promedio por producto: {precio_promedio_por_producto}")

#5. Ventas por Dia

ingresos_por_dia = {}
for venta in ventas:
    dia = venta['fecha']
    if dia in ingresos_por_dia:
        ingresos_por_dia[dia] += venta['precio'] * venta['cantidad']
    else:
        ingresos_por_dia[dia] = venta['precio'] * venta['cantidad']

print(f"Ingresos por dia: {ingresos_por_dia}")

#6. Representacion de Datos

resumen_ventas = {}
for venta in ventas:
    producto = venta['producto']
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            'cantidad_total': ventas_por_producto[producto],
            'ingresos_totales': precios_por_producto[producto][0],
            'precio_promedio': precio_promedio_por_producto[producto]
        }

print(f"Resumen de ventas: {resumen_ventas}")