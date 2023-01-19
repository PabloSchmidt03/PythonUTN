import pickle
import os.path
import random


class Cliente():
    def __init__(self, id, tipoc, tipop, monto):
        self.codigo = id
        self.tipo_cliente = tipoc
        self.tipo_pago = tipop
        self.monto = monto

    def __str__(self):
        r = "Codigo: {:<5}| Tipo de cliente: {:<3}| Tipo de pago: {:<3}| Monto: ${:>3} "
        return r.format(self.codigo, self.tipo_cliente, self.tipo_pago, self.monto)


def cargar_archivo(fd, n):
    m = open(fd, "wb")
    for i in range(n):
        codigo = random.randint(0, 10000)
        tipoc = random.randint(0, 3)
        tipop = random.randint(0, 9)
        monto = random.randint(100, 10000)
        cliente = Cliente(codigo, tipoc, tipop, monto)
        pickle.dump(cliente, m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error el archivo '" + str(fd) + "' no existe")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        cliente = pickle.load(m)
        print(cliente)
    m.close()


def crear_vector_filtrado(fd):
    v = []
    if not os.path.exists(fd):
        print("Error el archivo '" + str(fd) + "' no existe")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        cliente = pickle.load(m)
        if cliente.tipo_cliente == 0:
            v.append(cliente)
    m.close()
    return v


def mostrar_vector(v):
    for i in v:
        print(i)


def buscar_archivo(fd, x):
    if not os.path.exists(fd):
        print("Error el archivo '" + str(fd) + "' no existe")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        cliente = pickle.load(m)
        if cliente.codigo == x:
            return cliente
    m.close()
    return -1


def crear_matriz_conteo(fd):
    if not os.path.exists(fd):
        print("Error el archivo '" + str(fd) + "' no existe")
        return
    mat = [[0] * 10 for i in range(4)]
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        cliente = pickle.load(m)
        f = cliente.tipo_cliente
        c = cliente.tipo_pago
        mat[f][c] += 1
    m.close()


def mostrar_matriz(mat):
    hay = False
    r = "El tipo de clientes {:<2} que pagaron con la forma {:<2} son en total {}"
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            valor = mat[f][c]
            if valor % 2 != 0:
                print(r.format(f, c, mat[f][c]))
                hay = True
    return hay
