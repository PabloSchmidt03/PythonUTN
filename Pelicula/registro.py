import random
import pickle
import os
import os.path


class Produccion():
    def __init__(self, id, titulo, importe, tipo, pais):
        self.id = id
        self.titulo = titulo
        self.importe = importe
        self.tipo = tipo
        self.pais = pais

    def __str__(self):
        r = "{:<5}".format(str(self.id)) + "{:35}".format(str(self.titulo))
        r += "{:<10}".format(str(self.importe)) + "{:<2}".format(str(self.tipo))
        r += "{:>3}".format(str(self.pais))
        return r


def cargar_produccion():
    titulos = ("El increible ", "La maravillosa ", "La escalofriante ", "El maravilloso ")
    titulos2 = ("Spiderman ", "Tierra ", "Metodo Rebord ", "Pergolini ", "Ferrari ")
    id = random.randint(1, 10000)
    titulo = str(random.choice(titulos) + random.choice(titulos2) + str(random.randint(1, 5)))
    importe = random.randint(10000, 900000)
    tipo = random.randint(0, 9)
    pais = random.randint(0, 19)
    produccion = Produccion(id, titulo, importe, tipo, pais)
    return produccion


def crear_archivo(fd, v, imp):
    m = open(fd, "wb")
    for i in range(len(v)):
        if v[i].pais != 10 and v[i].importe < imp:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error, el archivo no existe")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        peli = pickle.load(m)
        print(peli)
    m.close()


def busqueda_secuencial_titulo(x, v):
    for i in range(len(v)):
        if v[i].titulo == x:
            return i
    return -1


def busqueda_secuencial_id(x, v):
    for i in range(len(v)):
        if v[i].id == x:
            return i
    return -1


def crear_matriz_conteo(v):
    matriz = [[0] * 20 for i in range(10)]
    for i in range(len(v)):
        f = v[i].tipo
        c = v[i].pais
        matriz[f][c] += 1
    return matriz


def mostrar_matriz(matriz):
    cad = 'Existen {:>5} peliculas para el tipo de pelicula {:>5} y pais de origen {:>5}'
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print(cad.format(f, c, matriz[f][c]))


def add_in_order(v, pelicula):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        mid = (izq + der) // 2
        if pelicula.titulo == v[mid].titulo:
            pos = mid
            break
        if pelicula.titulo < v[mid].titulo:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [pelicula]


def cargar_vector(n):
    v = []
    for i in range(n):
        produccion = cargar_produccion()
        add_in_order(v, produccion)
    return v


def validar_mayor(inf, mensaje="Ingrese cantidad de elementos: "):
    num = int(input(mensaje))
    while num <= inf:
        num = int(input('Error! ' + mensaje))
    return num


def mostrar_arreglo(v):
    for i in range(len(v)):
        print(v[i])
