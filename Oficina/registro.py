import random
import os
import os.path
import pickle


class Casos():

    def __init__(self, id, desc, monto, tipo, trib):
        self.id = id
        self.descripcion = desc
        self.monto = monto
        self.tipo = tipo
        self.tribunal = trib


    def __str__(self):
        r = str(self.id) + "    " + str(self.descripcion) + "    "  + str(self.monto) + "    "  + str(self.tipo) + "    "  + str(self.tribunal)
        return r


def crear_caso():
    nombre = 'Penal ', 'Civil ', 'Comercial ', 'Laboral ', 'Sucesion ', 'Quiebra ', 'Divocio '
    id = random.randint(0, 9999)
    descripcion = random.choice(nombre) + str(random.randint(1234, 4931))
    monto = random.randint(1, 100000)
    tipo = random.randint(0, 19)
    tribunal = random.randint(1, 10)
    caso = Casos(id, descripcion, monto, tipo, tribunal)
    return caso


def crear_vector(n):
    v = []
    for i in range(n):
        caso = crear_caso()
        add_in_order(v, caso)
    return v


def mostrar_vector(v):
    for caso in v:
        print(caso)



def add_in_order(v, caso):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if caso.id == v[mid].id:
            pos = mid
            break
        if caso.id < v[mid].id:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [caso]


def validar_mayor(inf, mensaje="Ingresar cantidad de elementos: "):
    n = int(input(mensaje))
    while n <= inf:
        print("Error, el numero ingresado debe ser mayor a ", inf)
        n = int(input(mensaje))
    return n


def busqueda_secuencial_desc(x, v):
    for i in range(len(v)):
        if v[i].descripcion == x:
            return i
    return -1


def crear_archivo(fd, v, x):
    m = open(fd, "wb")
    for i in range(len(v)):
        if v[i].tipo == 3 or v[i].tipo == 4 and v[i].monto < x:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(fd):
    i = 0
    if not os.path.exists(fd):
        print("Error, el archivo", fd, "no existe")
        return
    else:
        m = open(fd, "rb")
        size = os.path.getsize(fd)
        while m.tell() < size:
            caso = pickle.load(m)
            print(caso)
            i += 1
    m.close()
    print("Se mostraron", i, "registros")
