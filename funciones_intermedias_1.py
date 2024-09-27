#Funciones intermedias - Diego Amarilla - 26/09/24

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
print(matriz)
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)
ciudades["México"][2] = "Monterrey"
print(ciudades)
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

def iterarDiccionario(lista):
    for dicc in lista:
        salida = ', '.join([f"{llave} - {valor}" for llave, valor in dicc.items()])            
        print(salida)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

def iterarDiccionario2(llave, lista):
    for dicc in lista:
        if llave in dicc:
            print(dicc[llave])

print(iterarDiccionario2("pais", cantantes))

def imprimirInformacion(diccionario):
    for llave, valor in diccionario.items():
        print(f"{len(valor)} {llave.upper()}")
        print("\n".join(valor))

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print(imprimirInformacion(costa_rica))