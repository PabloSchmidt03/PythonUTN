from registro import *


def main():
    v = []
    fd = "videojuego.dat"
    op = -1
    while op != 6:
        print("\t\t\tMenu de opciones\n"
              "\t" + "-"*32 + "\n"
              "\t1)Cargar arreglo.\n"
              "\t2)Mostrar arreglo.\n"
              "\t3)Determinar la cantidad de juegos de cada pais por cada tipo.\n"
              "\t4)Crear un archivo.\n"
              "\t5)Mostrar el archivo.\n"
              "\t6)Salir.")
        op = int(input("Ingresar opcion: "))
        if op == 6:
            print("Adios!")
        elif op == 1:
            n = validar_mayor(0, "Ingresar la cantidad de videojuegos que desea cargar: ")
            crear_vector(n, v)
            print("Vector creado exitosamente!")
        elif len(v) > 0:
            if op == 2:
                x = validar_entre(-1, 21, "Ingrese pais de origen (un numero del 0 al 20): ")
                i = mostrar_vector_filtrado(v, x)
                if i == 0:
                    print("No se encontraron videojuegos con el pais de origen ingresado")
            elif op == 3:
                matriz = crear_matriz(v)
                x = validar_mayor(0, " Ingrese valor a comparar: ")
                mostrar_matriz(matriz, x)
            elif op == 4:
                crear_archivo(fd, v)
                print("Archivo creado exitosamente! ")
        if op == 5:
            mostrar_archivo(fd)
        if len(v) < 1 and 1 <= op <= 4:
            print("Error, primero se debe cargar el arreglo")
        if op > 6 or op == 0:
            print("Opcion incorrecta")


if __name__ == "__main__":
    main()