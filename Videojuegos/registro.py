import random
import pickle
import os
import os.path


class Videojuego():
    def __init__(self, id, nom, cant, precio, pais, tipo):
        self.id = id
        self.nombre = nom
        self.stock = cant
        self.precio = precio
        self.origen = pais
        self.tipo = tipo

    def __str__(self):
        r = str(self.id) + "  " + str(self.nombre) + "  " + str(self.stock)
        r += "  " + str(self.precio) + "  " + str(self.origen) + "  " + str(self.tipo)
        return r


def crear_registro():
    id = random.randint(0, 99999)
    nombre = "nombre " + str(random.randint(0, 99999))
    stock = random.randint(0, 9999)
    precio = random.randint(100, 900)
    origen = random.randint(0, 29)
    tipo = random.randint(0, 14)
    juego = Videojuego(id, nombre, stock, precio, origen, tipo)
    return juego


def crear_vector(n, v):
    for i in range(n):
        juego = crear_registro()
        add_in_order(juego, v)



def mostrar_vector_filtrado(v, x):
    i = 0
    for juego in v:
        if juego.origen == x:
            print(juego)
            i += 1
    return i



def add_in_order(juego, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if juego.nombre == v[mid].nombre:
            pos = mid
            break
        if juego.nombre < v[mid].nombre:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [juego]


def validar_mayor(inf, mensaje="Ingrese la cantidad de elementos: "):
    n = int(input(mensaje))
    while n <= inf:
        print("Error, el numero ingresado debe ser mayor a", inf)
        n = int(input(mensaje))
    return n


def validar_entre(inf, sup, mensaje="Ingrese la cantidad de elementos: "):
    n = int(input(mensaje))
    while inf >= n or sup <= n:
        print("Error, el numero ingresado debe estar entre", inf, "y", sup)
        n = int(input(mensaje))
    return n


def crear_matriz(v):
    matriz = [[0] * 15 for i in range(30)]
    for i in range(len(v)):
        f = v[i].origen
        c = v[i].tipo
        matriz[f][c] += 1
    return matriz


def mostrar_matriz(matriz, x):
    cad = 'Existen {:>3} Videojuegos para el pais de origen {:>3} y tipo {:>3}'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            valor = matriz[f][c]
            if 0 != valor < x:
                print(cad.format(matriz[f][c], f, c))


def crear_archivo(fd, v):
    m = open(fd, "wb")
    for juego in v:
        if juego.stock > 0 and juego.origen > 1:
            pickle.dump(juego, m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error, el archivo '" + str(fd) + "' no existe.")
    else:
        acu, cont = 0, 0
        m = open(fd, "rb")
        size = os.path.getsize(fd)
        while m.tell() < size:
            juego = pickle.load(m)
            acu += juego.precio
            cont += 1
            print(juego)
        m.close()
        promedio = acu / cont
        print("El promedio de todos los juegos es: " + str(round(promedio, 2)) + "$")