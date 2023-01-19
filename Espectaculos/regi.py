import pickle
import random
import os.path


class Evento():
    def __init__(self, id, tit, des, costo, tipo, seg):
        self.id = id
        self.titulo = tit
        self.descripcion = des
        self.costo = costo
        self.tipo_evento = tipo
        self.segmento_diario = seg

    def __str__(self):
        r = "Id: {:<3} - Titulo: {:<3} - Descripcion: {:<3} - Costo: {:<3} - Tipo de evento: {:<3} - Segmento diario: {:<3}"
        return r.format(self.id, self.titulo, self.descripcion, round(self.costo, 2), self.tipo_evento, self.segmento_diario)




def crear_evento():
    descripciones = ("El terremoto tuvo su epicentro en San Juan y se sintió en todo el norte argentino.",
                     "El terremoto tuvo su epicentro en San Juan y se sintió en todo el sur argentino.",
                     "El terremoto tuvo su epicentro en San Juan y se sintió en todo el oeste argentino.")
    letras = ("A", "B", "C", "D")
    id = str(random.randint(0, 1000)) + str(random.choice(letras))
    titulo = "Titulo " + str(random.randint(1, 90))
    descripciones = random.choice(descripciones)
    costo = random.uniform(1000, 90000)
    tipo = random.randint(0, 19)
    hora = random.randint(0, 9)
    evento = Evento(id, titulo, descripciones, costo, tipo, hora)
    return evento

def add_in_order(evento, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if evento.id == v[mid].id:
            pos = mid
            break
        elif evento.id < v[mid].id:
            der = mid - 1
        else:
            izq = mid + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [evento]


def crear_arreglo(n):
    v = []
    for i in range(n):
        evento = crear_evento()
        add_in_order(evento, v)
    return v


def mostrar_arreglo(v):
    for i in range(len(v)):
        print(v[i])


def generar_archivo(fd, v, p):
    m = open(fd, "wb")
    for evento in v:
        if evento.costo > p:
            pickle.dump(evento, m)
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("Error, el archivo no existe")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        evento = pickle.load(m)
        print(evento)
    m.close()


def recorrer_archivo(fd):
    v2 = []
    if not os.path.exists(fd):
        print("Error, el archivo no existe")
        return
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    while m.tell() < size:
        evento = pickle.load
        if evento.tipo_evento > 5:
            v2.append(evento.costo)
    m.close()
    return v2


def arreglo_montos_produccion(nombre_archivo):
    v = []

    if not os.path.exists(nombre_archivo):
        print('No existe un archivo generado con el nombre {}\n'.format(nombre_archivo))
        return v

    m = open(nombre_archivo, 'rb')
    size = os.path.getsize(nombre_archivo)
    while m.tell() < size:
        evento = pickle.load(m)
        if evento.tipo_evento > 5:
            v.append(evento.costo)
    m.close()
    return v


def busqueda_binaria(v, cod):
    n = len(v)
    izq, der = 0, n-1
    while izq <= der:
        mid = (izq + der) // 2
        if v[mid].id == cod:
            print(v[mid])
            return v[mid].descripcion
        elif v[mid].id > cod:
            der = mid - 1
        else:
            izq = mid + 1
    return -1


def crear_matriz(v):
    mat = [[0] * 10 for i in range(20)]
    for i in range(len(v)):
        f = v[i].tipo_evento
        c = v[i].segmento_diario
        mat[f][c] += 1
    return mat


def mostrar_matriz(mat):
    r = "Para el tipo de evento: {}, en el rango horario: {}, hay {} eventos."
    for f in range(8, len(mat)):
        for c in range(len((mat[f]))):
            if mat[f][c] > 0:
                print(r.format(f, c, mat[f][c]))


def procesar_caracteres(cadena):
    cont_letras = 0
    cont_palabras_mayus_t_s = 0
    empieza_may = False
    tienets = False
    for car in cadena:
        if car != " " and car != ".":
            cont_letras += 1
            if cont_letras == 1 and "A" < car < "Z":
                empieza_may = True
            if car == t or car == s:
                tienets = True
        else:
            if cont_letras > 0:
                if empieza_may and tienets:
                    cont_palabras_mayus_t_s += 1
            cont_letras = 0
            empieza_may, tienets = False, False
    print("Cantidad de palabras comenzadas con mayuscula y que tienen 't' o 's': ", cont_palabras_mayus_t_s)


def vector_conteo(v):
    v_cont = [0] * 20
    for i in v:
        v_cont[i.tipo_evento] += 1
    return v_cont


def mostrar_vector_conteo(v):
    for i in range(len(v)):
        if v[i] > 0:
            print("Para el tipo", i, "hay", v[i], "Eventos")

def validar_mayor(inf, msj="Ingresar cantidad"):
    n = int(input(msj))
    while n <= inf:
        print("Error, debe ser mayor a", inf)
        n = int(input(msj))
    return n


def calcular_prom(v):
    acu, cont = 0, 0
    for evento in v:
        acu += evento
        cont += 1
    if cont > 0:
        prom = acu / cont
    else:
        prom = 0
    return prom



