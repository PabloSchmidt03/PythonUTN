from registro import *


def main():
    v = list()
    op = -1
    fd = "polizas.dat"
    while op != 6:
        print("Menu de opciones: \n"
              "\t 1) Cargar los datos en el registro. \n"
              "\t 2) Mostrar registros. \n"
              "\t 3) Matriz de conteo. \n"
              "\t 4) Crear un archivo. \n"
              "\t 5) Mostrar archivo. ")
        op = int(input("Ingrese su opcion: "))
        if op == 1:
            n = validar_mayor(0)
            v = crear_vector(n)
            print("Vector cargado exitosamente")
        elif len(v) > 0:
            if op == 2:
                x = validar_entre(0, 6)
                hay = mostrar_vector_filtrado(v, x)
                if not hay:
                    print("No se encontro ningun registro")
            elif op == 3:
                mat = crear_matriz(v)
                tp = validar_entre(-1, 20)
                mostrar_matriz_filtrada(mat, tp)
            elif op == 4:
                x = validar_mayor(0, "Ingrese el precio de la poliza a comparar: ")
                generar_archivo(fd, v, x)
                print("Archivo creado exitosamente")
        elif op == 5:
            mostrar_archivo(fd)
        elif op == 6:
            print("Adios")
        elif len(v) == 0 and 2 <= op <= 4:
            print("Error, primero debe cargar el arreglo")
        if 1 < op > 6:
            print("Error, opcion incorrecta")



if __name__ == "__main__":
    main()