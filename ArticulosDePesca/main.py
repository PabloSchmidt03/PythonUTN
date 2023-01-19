from registro import *


def main():
    v = []
    fd = "pesca.dat"
    op = -1
    while op != 7:
        print("\t\t\tMenu de opciones\n"
              "\t1)Crear arreglo.\n"
              "\t2)Mostrar arreglo filtrado.\n"
              "\t3)Buscar en el arreglo.\n"
              "\t4)Crear archivo.\n"
              "\t5)Mostrar archivo.\n"
              "\t6)Crear y mostrar matriz de conteo.\n"
              "\t7)Salir.")
        op = validar_entre(0, 8)
        if op == 1:
            n = validar_mayor(0, "Ingrese la cantidad de articulos que desea cargar: ")
            v = crear_vector(n)
            print("Vector creado exitosamente!!")
        elif len(v) > 0:
            if op == 2:
                x = validar_entre(0, 24, "Ingresar numero de origen a comparar: ")
                hay = mostrar_vector_filtrado(v, x)
                if not hay:
                    print("No existe ningun articulo con lugar de origen distinto de", x)
            elif op == 3:
                num = validar_mayor(-1, "Ingrese id del articulo a buscar: ")
                input("Presione Enter para buscar el articulo..\n")
                i = busqueda_secuen(v, num)
                if i != -1:
                    print("Artículo encontrado!")
                    print(v[i], "\n")
                else:
                    print("No se encontró ningun articulo con ese id")
            elif op == 4:
                x = validar_entre(0, 29, "Ingresar numero de tipo de articulo: ")
                crear_archivo_filtrado(v, fd, x)
                print("Archivo creado exitosamente!")
            elif op == 6:
                generar_matriz(v)
                print("-"*200)
                crear_matriz(v)
        if op == 5:
            mostrar_archivo(fd)



if __name__ == "__main__":
    main()