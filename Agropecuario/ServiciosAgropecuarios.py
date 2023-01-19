from RegistroServiciosAgropecuarios import *


def main():
    v = []
    fd = "servicios.dat"
    op = -1
    while op != 0:
        op = mostrar_menu()
        if op == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de operaciones agricolas que desea cargar: ")
            v = cargar_arreglo(n)
            mostrar_vector(v, 1)
        elif op == 0:
            print("Hasta luego!")
        elif len(v) == 0:
            print("Error, primero debe cargar el vector")
        elif op == 2:
            z = validar_entre(0, 19, "Ingresar numero a comparar: ")
            mostrar_vector(v, z)
        elif op == 3:
            matriz = generar_matriz(v)
            v1 = int(input("Ingresar nro: "))
            v2 = int(input("Ingresar nro: "))
            mostrar_matriz(matriz, v1, v2)
        elif op == 4:
            generar_archivo(v, fd)
        elif op == 5:
            mostrar_archivo(fd)



if __name__ == "__main__":
    main()