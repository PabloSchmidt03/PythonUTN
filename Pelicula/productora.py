from registro import *


def main():
    v = list()
    op = -1
    fd = "peliculas.dat"
    while op != 0:
        print("Menu de opciones: \n"
              "\t 1) Cargar los datos en el registro. \n"
              "\t 2) Mostrar el registro. \n"
              "\t 3) Buscar un registro por titulo. \n"
              "\t 4) Crear un archivo. \n"
              "\t 5) Mostrar archivo. \n"
              "\t 6) Buscar un registro por id \n"
              "\t 7) Determinar cantidad de peliculas por cada posible pais de origen")
        op = int(input("Ingrese su opcion: "))
        if op == 1:
            n = validar_mayor(0, "Ingrese la cantidad de producciones: ")
            v = cargar_vector(n)
            print("Arreglo cargado exitosamente")
        elif op == 0:
            print("Adios!")
        elif len(v) > 0:
            if op == 2:
                mostrar_arreglo(v)
            elif op == 3:
                titulo = input("Ingrese el titulo que desea buscar: ")
                indice = busqueda_secuencial_titulo(titulo, v)
                if indice != -1:
                    v[indice].importe = validar_mayor(0, "Ingrese el nuevo importe de la pelicula: ")
                    print(v[indice])
                else:
                    print("No existe ninguna pelicula con ese titulo")
            elif op == 4:
                imp = int(input("Ingrese el importe que desea comparar: "))
                crear_archivo(fd, v, imp)
                print("Archivo generado exitosamente")
            elif op == 5:
                mostrar_archivo(fd)
            elif op == 6:
                id = int(input("Ingrese el numero de pelicula que desea buscar: "))
                indice = busqueda_secuencial_id(id, v)
                if indice != -1:
                    print(v[indice])
                else:
                    print("No existe ninguna pelicula con ese titulo")
            elif op == 7:
                matriz = crear_matriz_conteo(v)
                mostrar_matriz(matriz)
        elif len(v) == 0 and 2 <= op <= 7:
            print("Error, el vector no esta cargado")
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
