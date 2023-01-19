from registros import *


def main():
    v = []
    fd = "agropecuario.dat"
    op = -1
    while op != 6:
        print("Menu")
        print("Opcion 1).")
        print("Opcion 2).")
        print("Opcion 3).")
        print("Opcion 4).")
        print("Opcion 5).")
        print("Opcion 6).")
        op = int(input("Ingresar opcion: "))
        if op == 1:
            n = int(input("Ingresar cantidad de registros: "))
            v = cargar_vector(n)
        if len(v) > 0:
            if op == 2:
                z = int(input("Ingresar zona: "))
                mostrar_vector_filtrado(v, z)
            elif op == 3:
                mat = crear_matriz(v)
                v1 = int(input("Ingresar valor: "))
                v2 = int(input("Ingresar valor: "))
                mostrar_matriz_filtrada(mat, v1, v2)
            elif op == 4:
                prom = sacar_prom(v)
                crear_archivo(fd, v, prom)
                print("Archivo generado, solo con los importes mayores a $" + str(round(prom, 2)))
        if op == 5:
            mostrar_archivo(fd)


if __name__ == "__main__":
    main()