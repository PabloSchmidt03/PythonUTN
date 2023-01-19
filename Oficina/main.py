from registro import *


def main():
    v = []
    op = -1
    fd = "datos.dat"
    while op != 6:
        print("\t\t\tMenu de opciones\n"
              "\t 1) Cargar arreglo.\n"
              "\t 2) Mostrar el arreglo.\n"
              "\t 3) Buscar un registro por descripción.\n"
              "\t 4) Crear un archivo a partir del arreglo. \n"
              "\t 5) Mostrar el archivo.\n"
              "\t 6) Salir.")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            n = validar_mayor(0, "Ingrese la cantidad de casos que desea cargar: ")
            v = crear_vector(n)
            print("Arreglo cargado exitosamente!")
        if len(v) > 0:
            if op == 2:
                mostrar_vector(v)
            elif op == 3:
                x = input("Ingresar descripcion a buscar: ")
                index = busqueda_secuencial_desc(x, v)
                if index != -1:
                    print(v[index])
                else:
                    print("No se encontró ningun caso con la descripción ingresada")
            elif op == 4:
                monto = validar_mayor(0, "Ingrese monto a comparar: ")
                crear_archivo(fd, v, monto)
                print("Archivo creado exitosamente!")
        if op == 5:
            mostrar_archivo(fd)
        elif op == 6:
            print("Adios! ")
        if len(v) == 0 and 2 <= op <= 4:
            print("Error! Primero debe cargar el arreglo. (opcion 1)")





if __name__ == "__main__":
    main()