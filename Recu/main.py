# 19/09/22 TIPO PARCIAL, CLASE TEORICA.
from registro import *
import os
import pickle
import random


def grabar_archivo(fd, n):
    m = open(fd, "wb")
    for i in range(n):
        # Se generan los datos del cliente de manera automática.
        cod = i + 1
        tipo = random.randint(0, 3)
        pago = random.randint(0, 9)
        monto = random.randint(1000, 5000)
        cli = Cliente(cod, tipo, pago, monto)
        pickle.dump(cli, m)
        # Vuelca los datos del buffer para que se graben en disco..
        m.flush()
    print('Finalizado el proceso de grabación del archivo!!!')
    m.close()


def listado_completo(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return

    tam = os.path.getsize(fd)
    m = open(fd, 'rb')
    print('Listado general de clientes registrados:')
    while m.tell() < tam:
        cli = pickle.load(m)
        print(cli)
    m.close()
    print()
    input('Presione <Enter> para seguir...')


def generar_lista(fd):
    lista = []
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < tam:
        cli = pickle.load(m)
        if cli.tipo == 0:
            lista.append(cli)
    m.close()
    return lista


def mostrar_lista(lista):
    if len(lista) > 0:
        for i in range(len(lista)):
            print(lista[i])
    else:
        print('No se pudo generar el vector no hay clientes tipo normal')


def generar_matriz(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    matriz_conteo = [[0] * 10 for i in range(4)]
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < tam:
        cli = pickle.load(m)
        # Obtengo los indices para acceso directo a la matriz
        fila = cli.tipo
        col = cli.pago
        # Hago el conteo en la matriz
        matriz_conteo[fila][col] += 1
    m.close()
    return matriz_conteo


def mostrar_matriz(conteo):
    for i in range(len(conteo)):
        for j in range(len(conteo[i])):
            # Filtro el contenido impar..
            if conteo[i][j] % 2 != 0:
                print('La cantidad de clientes de tipo:', i, ' y tipo forma pago ', j, ' es:', conteo[i][j])


def buscar_cliente(lista_nueva, cod):
    for i in range(len(lista_nueva)):
        if lista_nueva[i].codigo == cod:
            return i
    return -1


def generar_vector_acumulacion(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    vec_acu = 4 * [0]
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < tam:
        cli = pickle.load(m)
        # Hago la acumulación en el vector
        vec_acu[cli.tipo] += cli.monto
    m.close()
    return vec_acu


def mostrar_vector_acu(acu):
    for i in range(len(acu)):
        if acu[i] > 0:
            print('Cliente ', i, ' el importe total es $:', acu[i])


def test():
    global lista_nueva
    fd = 'clientes.dat'
    lista = []
    op = 0
    while op != 7:
        print('Ejercicio manejo de archivo de clientes')
        print('   1. Grabar clientes en archivo')
        print('   2. Mostrar contenido archivo clientes')
        print('   3. Generar un vector a partir con clientes tipo normal')
        print('   4. Búsqueda en el vector por código de cliente')
        print('   5. Generar matriz de conteo')
        print('   6. Generar vector de acumulación')
        print('   7. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            n = int(input('Ingrese la cantidad de clientes:'))
            grabar_archivo(fd, n)
        elif op == 2:
            listado_completo(fd)
        elif op == 3:
            lista_nueva = generar_lista(fd)
            print('Clientes de clientes tipo normal del vect. generado:')
            mostrar_lista(lista_nueva)
        elif op == 4:
            cod = int(input('Ingrese el código a buscar:'))
            pos = buscar_cliente(lista_nueva, cod)
            if pos == -1:
                print('Cliente no encontrado')
            else:
                print('El tipo que pago cliente:', lista_nueva[pos].pago, ' el monto de compra es:',
                      lista_nueva[pos].monto)
        elif op == 5:
            conteo = generar_matriz(fd)
            mostrar_matriz(conteo)
        elif op == 6:
            acu = generar_vector_acumulacion(fd)
            mostrar_vector_acu(acu)
        elif op == 7:
            print('Programa Finalizado...')


# script principal...
if __name__ == '__main__':
    test()
