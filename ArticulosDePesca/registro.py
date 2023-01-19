import random
import pickle
import os.path


class Articulo():
    def __init__(self, id, des, prc, origen, tipo):
        self.id = id
        self.descripcion = des
        self.precio = prc
        self.origen = origen
        self.tipo = tipo

    def __str__(self):
        r = str(self.id) + " " + str(self.descripcion) + " $" + str(self.precio) + " " + str(self.origen) + " " + str(self.tipo)
        return r


def crear_articulo():
    id = random.randint(0, 999)
    des = "Descripcion " + str(random.randint(0, 10000))
    precio = random.randint(1000, 9000)
    origen = random.randint(0, 24)
    tipo = random.randint(0, 29)
    articulo = Articulo(id, des, precio, origen, tipo)
    return articulo


def add_in_order(v, r):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if r.id == v[mid].id:
            pos = mid
            break
        if r.id <= v[mid].id:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [r]


def crear_vector(n):
    v = []
    for i in range(n):
        articulo = crear_articulo()
        add_in_order(v, articulo)
    return v


def validar_entre(inf, pos, msj="Ingrese opcion: "):
    n = int(input(msj))
    while inf > n or n > pos:
        print("Error, el numero debe estar entre", inf, "y", pos)
        n = int(input(msj))
    return n


def validar_mayor(inf, msj="Ingrese cantidad de elementos: "):
    n = int(input(msj))
    while inf > n:
        print("Error, el numero debe ser mayor", inf)
        n = int(input(msj))
    return n


def mostrar_vector_filtrado(v, x):
    hay = False
    for articulo in v:
        if articulo.origen != x:
            print(articulo)
            hay = True
    return hay


def busqueda_secuen(v, x):
    for i in range(len(v)):
        if v[i].id == x:
            return i
    return -1


def crear_archivo_filtrado(v, fd, x):
    m = open(fd, "wb")
    for i in range(len(v)):
        if v[i].tipo != x:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(fd):
    i = 0
    acu = 0
    if not os.path.exists(fd):
        print("Error, el archivo no esta creado :(")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        articulo = pickle.load(m)
        print(articulo)
        i += 1
        acu += articulo.precio
    m.close()
    prom = acu / i
    print("Se mostraron", i, "articulos")
    print("El precio promedio es: $" + str(round(prom, 2)))


def crear_matriz(v):
    matriz = [[0] * 25 for i in range(30)]
    for art in v:
        f = art.tipo
        c = art.origen
        matriz[f][c] += art.precio

    r = "{:>4}  {:<3}  {:<3}"
    for f in range(2, 11):
        for c in range(4, 16):
            if matriz[f][c] > 0:
                print(r.format(matriz[f][c], c, f))



def generar_matriz(vector):
    mat = [[0] * 30 for i in range(25)]
    for articulo in vector:
        f = articulo.origen
        c = articulo.tipo
        mat[f][c] += articulo.precio

    print('Ver acumuladores distintos de cero')
    for f in range(4, 16):
        for c in range(2, 11):
            if mat[f][c] != 0: # and 4 <= f <= 15 and 2 <= c <= 10:
                print('Precio de Venta para el origen {} tipo {} es '
                      'de ${:<10.2f}'.format(f, c, mat[f][c]))
