import random
import os.path
import os
import pickle


class Operacion():
    def __init__(self, id, desc, importe, tipo, campo):
        self.id = id
        self.desc = desc
        self.importe = importe
        self.tipo = tipo
        self.campo = campo


    def __str__(self):
        r = "| ID: " + str(self.id) + "{:<26}".format("| Descripcion: " + str(self.desc)) + "{:<15}".format("| Importe: " + str(self.importe))
        r += "{:<10}".format("| Tipo: " + "{:>2}".format(str(self.tipo))) + "| Campo: " + "{:>2}".format(str(self.campo))
        return r


def cargar_registro():
    desc = ('Regar', 'Desmalezar', 'Cosechar', 'Sembrar')
    numero = random.randint(10, 99)
    descripcion = random.choice(desc)
    importe = random.randint(100, 200)
    tipo = random.randint(1, 15)
    zona = random.randint(0, 19)
    operacion = Operacion(numero, descripcion, importe, tipo, zona)
    return operacion


def cargar_arreglo(n):
    v = []
    for i in range(n):
        operacion = cargar_registro()
        add_in_order(operacion, v)
    return v


def add_in_order(reg, v):
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].id == reg.id:
            pos = c
            break
        if reg.id > v[c].id:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [reg]


def mostrar_menu():
    print('\nSERVICIOS AGROPECUARIOS')
    print('1. Cargar')
    print('2. Mostrar')
    print('3. Generar matriz')
    print('4. Generar archivo')
    print('5. Mostrar archivo')
    print('0. Salir')
    opcion = int(input('Ingrese opcion: '))
    return opcion


def validar_mayor_que(lim, mensaje):
    num = int(input(mensaje))
    while num < lim:
        num = int(input('Error! ' + mensaje))
    return num


def mostrar_vector(v, z):
    for reg in v:
        if reg.campo >= z:
            print(reg)


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        num = int(input('Error! ' + mensaje))
    return num


def generar_matriz(v):
    # matriz de conteo de 15 * 20
    m = [[0] * 20 for f in range(15)]
    # Cuántas operaciones de cada tipo (1-15)
    # se hicieron en cada posible zona (0-19)
    for i in range(len(v)):
        fila = v[i].tipo - 1
        col = v[i].zona
        m[fila][col] += 1
    return m


def mostrar_matriz(m, v1, v2):
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] > v1 and m[f][c] < v2:
                print('Tipo', f, 'Zona', c, ':', m[f][c])


def calcular_promedio(v):
    suma = 0
    for i in range(len(v)):
        suma += v[i].importe
    return suma / len(v)


def generar_archivo(v, fd):
    prom = calcular_promedio(v)
    m = open(fd, 'wb')
    for i in range(len(v)):
        if v[i].importe > prom:
            pickle.dump(v[i], m)
    m.close()
    print('Archivo generado para promedio mayor a', round(prom, 2))


def mostrar_archivo(fd):
    cont = 0
    if os.path.exists(fd):
        m = open(fd, 'rb')
        tam = os.path.getsize(fd)
        while m.tell() < tam:
            reg = pickle.load(m)
            print(reg)
            cont += 1
        m.close()
        print('Se mostraron', cont, 'registros')
    else:
        print('El archivo', fd, 'no existe')