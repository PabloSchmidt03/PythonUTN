from registro import *

"""Enunciado integrador: Desarrollar un programa gestione los clientes de una empresa en un archivo.
De cada Cliente se necesita registrar: un código, tipo de cliente (0. Normal 1. Habitual 2.Especial 3.Moroso),
tipo de pago (un valor entero cuyo rango es del 0 al 9) y monto de la compra.

1) Grabar los clientes (alta) en un archivo. La cantidad de clientes debe ser ingresada por teclado.
2) Listar el archivo con todos los clientes registrados.
3) A partir del archivo creado en el punto 1 generar un vector que contenga los clientes
que sean tipo 0 (Normal). Mostrar el vector resultante.
4) Determinar si existe un cliente cuyo código de cliente es igual a "c" que debe ser ingresado
por teclado. En caso de encontrarlo mostrar su forma que pago y el monto de la compra, sino lo encuentra
informar con un mensaje de error.
5) A partir del archivo determinar cuantos clientes tiene la empresa por tipo de cliente(EL PRIMER DATO ES FILA) y forma
de pago(((COLUMNA))) que realiza, es decir 40 contadores.Mostrar solo los conteos de la matriz que sean impares.
6) A partir de los datos del archivo determinar el importe total que recaudó la empresa por tipo de
cliente, es decir 4 acumuladores (usar un vector de acumulación).
Mostrar solo las acumulaciones que sean distinta de cero."""
"""    for cliente in m:
        if cliente[-1] == "\n":
            cliente = cliente[:-1]
        cadenas = cliente.split("\n")
        if cadenas[1] == 0:
            codigo = cadenas[0]
            tipo_c = cadenas[1]
            tipo_p = cadenas[2]
            monto = cadenas[3]
            cliente = Cliente(codigo, tipo_c, tipo_p, monto)
            pickle.dump(cliente, v)"""

def main():
    v = []
    fd = "clientes.dat"
    op = -1
    while op != 7:
        print("\nMenu de opciones\n"
              "1) Grabar un archivo\n"
              "2) Listar el archivo\n"
              "3) Generar vector con clientes de tipo 0\n"
              "4) Determinar si existe un cliente por codigo\n"
              "5) Determinar cuantos clientes tiene la empresa por cada tipo de cliente y forma de pago\n"
              "6) Determinar el importe total por tipo de cliente\n"
              "7) Salir\n")
        op = int(input("Ingresar opcion: "))
        if op == 1:
            n = int(input("Ingresar cantidad de clientes: "))
            cargar_archivo(fd, n)
            print("Clientes cargados! ")
        elif op == 2:
            mostrar_archivo(fd)
        elif op == 3:
            v = crear_vector_filtrado(fd)
            mostrar_vector(v)
        elif op == 4:
            r = "Tipo de pago: {} \nMonto: ${}"
            x = int(input("Ingrese codigo de cliente: "))
            cliente = buscar_archivo(fd, x)
            if cliente != -1:
                print("Cliente encontrado! ")
                print(r.format(cliente.tipo_pago, cliente.monto))
            else:
                print("error")
        elif op == 5:
            mat = crear_matriz_conteo(fd)
            hay = mostrar_matriz(mat)
            if not hay:
                print("No hay ninguna matriz impar :(")



if __name__ == "__main__":
    main()
