import os.path
import pickle

def add_in_order(paciente, vector):
    n = len(vector)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if paciente.id == vector[mid].id:
            pos = mid
            break
        elif paciente.id < vector[mid].id:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [paciente]

#Matriz de 10 * 5
def crear_matriz(v):
    mat = [[0] * 5 for i in range(10)]
    for i in range(len(v)):
        f = v[i].tipo
        c = v[i].monto
        mat[f][c] += 1
    return mat


def mostrar_mat(mat):
    r = "Para el tipo {:<3} y el monto {:<3}, hay {:<3} cosas"
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(r.format(f, c, mat[f][c]))


def generar_matriz_archivo(fd):
    if not os.path.exists(fd):
        print("Error")
        return
    m = open(fd, "wb")
    mat = [[0] * 5 for i in range(10)]
    size = os.path.getsize(fd)
    while m.tell() < size:
        registro = pickle.load(m)
        fila = registro.tipo
        columna = registro.campo
        mat[fila][columna] += 1
    m.close()
    return mat


def vector_conteo(v):
    v_cont = [0] * 24
    for i in range(len(v)):
        v_cont[v[i].id] += v[i].monto
    return v_cont
