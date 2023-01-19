from reg import *


def main():
    v = []
    fd = "parcial.dat"
    op = -1
    while op != 9:
        print("Op 1")
        print("Op 2")
        print("Op 3")
        print("Op 4")
        print("Op 5")
        print("Op 6")
        print("Op 7")
        print("Op 8")
        print("Op 9")
        op = int(input("Ingresar opcion"))
        if op == 1:
            n = validar_mayor(0)
            v = crear_vector(n)
            print("Vector creado exitosamente")
        if len(v) > 0:
            if op == 2:
                mostrar_vector(v)
            elif op == 3:
                m = int(input("Ingresar monto a comparar"))
                v2 = crear_vector_filtrado(v, m)
                seleccion_directa(v)
                mostrar_vector(v2)
            elif op == 4:
                v3 = crear_vector_conteo(v)
                mostrar_vector_filtrado(v3)
            elif op == 7:
                h = validar_mayor(0)
                p = input("Ingresar patente")
                pos = busqueda_secuencial(v, p, h)
                if pos != -1:
                    puesto = v[pos].nombre
                else:
                    print("No existe")
            elif op == 8:
                cadena(puesto)
        if op == 5:
            id = validar_mayor(0)
            crear_archivo(fd, v, id)
        elif op == 6:
            mostrar_archivo(fd)


if __name__ == "__main__":
    main()
