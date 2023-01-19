import random
import os
import os.path
import pickle


class Poliza():
    def __init__(self, cod, desc, precio, tipo, forma):
        self.codigo = cod
        self.descripcion = desc
        self.precio = precio
        self.tipo = tipo
        self.formapago = forma

    def __str__(self):
        r = str(self.codigo) + " " + str(self.descripcion) + " " + str(self.precio) + " " + str(self.tipo) + " "
        r += str(self.formapago)
        return r


def generar_poliza():
    cod = random.randint(0, 10000)
    descripcion = "Descripción " + str(random.randint(1, 99999))
    precio = random.randint(100, 10000)
    tipo = random.randint(0, 19)
    forma = random.randint(1, 5)
    poliza = Poliza(cod, descripcion, precio, tipo, forma)
    return poliza


def crear_vector(n):
    v = []
    for i in range(n):
        poliza = generar_poliza()
        add_in_order(v, poliza)
    return v


def mostrar_vector_filtrado(v, x):
    hayuno = False
    for i in range(len(v)):
        if v[i].formapago != x:
            print(v[i])
            hayuno = True
    return hayuno


def crear_matriz(v):
        matriz = [[0] * 5 for i in range(20)]
        for i in range(len(v)):
            f = v[i].tipo
            c = v[i].formapago - 1
            matriz[f][c] += 1
        return matriz


def mostrar_matriz_filtrada(matriz, tp):
    r = " Hay {:<3} polizas para el tipo de poliza {:<3} y forma de pago {:<3}"
    for f in range(len(matriz)):
        if f != tp:
            for c in range(len(matriz[f])):
                if matriz[f][c] > 0:
                    print(r.format(matriz[f][c], f, c + 1))


def add_in_order(v, poliza):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if poliza.descripcion == v[mid].descripcion:
            pos = mid
            break
        if poliza.descripcion < v[mid].descripcion:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [poliza]


def validar_mayor(inf, msj="Ingrese la cantidad de registros que desee cargar: "):
    n = int(input(msj))
    while n <= inf:
        print("Error, el numero ingresado debe ser mayor a", inf)
        n = int(input(msj))
    return n


def validar_entre(inf, sup):
    n = int(input("Ingrese numero a comparar: "))
    while n <= inf or n >= sup:
        print("Error, el numero ingresado debe estar entre", inf, "y", sup )
        n = int(input("Ingrese numero a comparar: "))
    return n


def generar_archivo(fd, v, p):
    m = open(fd, "wb")
    for i in range(len(v)):
        if v[i].precio > p:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error, el archivo '" + str(fd) + "' no existe..")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        poliza = pickle.load(m)
        print(poliza)
    m.close()
