import random
import os.path
import pickle

class Cobros():
    def __init__(self, id, nom, monto, patente, hora):
        self.id = id
        self.nombre = nom
        self.monto = monto
        self.patente = patente
        self.hora = hora

    def __str__(self):
        r = "Id: {:<4} - Nombre: {:<4} - Monto: {:<4} - Patente: {:<4} - Hora: {:<4} - "
        return r.format(self.id, self.nombre, self.monto, self.patente, self.hora)


def generar_caso():
    nombres = ("Autopista Carlos Paz.", "Córdoba acceso norte.", "Autopista Carlos Dryon.", "Autopista Carlos Bianchi.",)
    patente = ("AAA", "ABF", "PDS", "FDS", "GGT")
    id = random.randint(0, 10000)
    nombre = random.choice(nombres)
    monto = random.randint(100, 900)
    patente = random.choice(patente) + str(random.randint(100, 999))
    hora = random.randint(0, 23)
    return Cobros(id, nombre, monto, patente, hora)


def crear_vector(n):
    v = []
    for i in range(n):
        cobro = generar_caso()
        v.append(cobro)
    return v


def crear_vector_filtrado(v, m):
    v2 = []
    for i in range(len(v)):
        if v[i].monto < m:
            v2.append(v[i])
    return v2


def validar_mayor(inf):
    n = int(input("Ingresar cantidad de casos"))
    while n <= inf:
        print("Error, el numero debe ser mayor a", inf)
        n = int(input("Ingresar cantidad de casos"))
    return n


def mostrar_vector(v):
    for i in v:
        print(i)


def seleccion_directa(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]


def crear_vector_conteo(v):
    v_cont = [0] * 24
    for i in range(len(v)):
        v_cont[v[i].hora] += v[i].monto
    return v_cont


def mostrar_vector_filtrado(v):
    for i in range(len(v)):
        if 0 <= i <= 6 or 20 <= i <= 23:
            if v[i] > 0:
                print("Monto total recaudado a las", i, ":", v[i])


def crear_archivo(fd, v, id):
    m = open(fd, "wb")
    for reg in v:
        if reg.id == id:
            pickle.dump(reg, m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error")
        return None
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        reg = pickle.load(m)
        print(reg)


def busqueda_secuencial(v, p, h):
    for i in range(len(v)):
        if v[i].patente == p and v[i].hora == h:
            return i
    return -1


def es_may(car):
    if "A" <= car <= "Z":
        return True
    return False


def cadena(cadena):
    cont_palabras_con_mayuscula = 0
    tiene_may = False
    for car in cadena:
        if car != " " and car != ".":
            if es_may(car):
                tiene_may = True
        else:
            if tiene_may:
                cont_palabras_con_mayuscula += 1
            tiene_may = False
    print(cont_palabras_con_mayuscula)

