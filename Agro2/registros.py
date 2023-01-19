import random
import os.path
import pickle


class Agropecuario():
    def __init__(self, id, desc, imp, tipo, zona):
        self.id = id
        self.descripcion = desc
        self.importe = imp
        self.tipo = tipo
        self.zona = zona

    def __str__(self):
        r = "ID: {:<30} - DESCRIPCION: {:<30} - IMPORTE: {:<30} - TIPO: {:<30} - ZONA: {:<30}"
        return r.format(self.id, self.descripcion, self.importe, self.tipo, self.zona)


def cargar_operacion():
    id = random.randint(0, 100)
    desc = "Descripcion" + str(random.randint(0, 100))
    importe = random.randint(900, 10000)
    tipo = random.randint(1, 15)
    zona = random.randint(0, 19)
    return Agropecuario(id, desc, importe, tipo, zona)


def add_in_order(r, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if r.id == v[mid].id:
            pos = mid
            break
        elif r.id < v[mid].id:
            der = mid -1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [r]


def cargar_vector(n):
    v = []
    for i in range(n):
        agro = cargar_operacion()
        add_in_order(agro, v)
    return v


def mostrar_vector_filtrado(v, x):
    for i in v:
        if i.zona >= x:
            print(i)


def crear_matriz(v):
    mat = [[0] * 20 for i in range(15)]
    for i in range(len(v)):
        f = v[i].tipo - 1
        c = v[i].zona
        mat[f][c] += 1
    return mat


def crear_matriz_repe(v):
    mat = [[0] * 20 for i in range(15)]
    for i in range(len(v)):
        f = v[i].tipo - 1
        c = v[i].zona
        mat[f][c] += 1
    return mat


def mostrar_matriz_repe(mat):
    for f in range(mat):
        for c in range(mat[f]):
            print(f + 1, c, mat[f][c])

def mostrar_matriz_filtrada(mat, v1, v2):
    r = "Para el tipo {:<4} y la zona {:<4} hay {:<4} operaciones"
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if v1 < mat[f][c] < v2:
                print(r.format(f, c, mat[f][c]))


def sacar_prom(v):
    ac = cont = 0
    for i in range(len(v)):
        ac += v[i].importe
        cont += 1
    prom = ac / cont
    return prom


def crear_archivo(fd, v, prom):
    m = open(fd, "wb")
    for i in range(len(v)):
        if v[i].importe > prom:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error pa")
        return
    else:
        cont = 0
        m = open(fd, "rb")
        size = os.path.getsize(fd)
        while m.tell() < size:
            agro = pickle.load(m)
            cont += 1
            print(agro)
        print("Se mostraron", cont, "registros")
