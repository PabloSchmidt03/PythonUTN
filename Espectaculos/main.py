from regi import *


def main():
    v = []
    v2 = []
    fd = "recu.dat"
    op = -1
    while op != 9:
        print("\n Menu de opciones \n"
              "1) Crear arreglo\n"
              "2) Mostrar\n"
              "3) Generar registro\n"
              "4) Mostrar archivo\n"
              "5) Generar vector a partir del archivo\n"
              "6) Buscar por id\n"
              "7) Matriz de conteo\n"
              "8) Procesar caracteres\n"
              "9) Salir")
        op = int(input("Ingresar opcion: "))
        if op == 1:
            n = validar_mayor(0, "Ingresar la cantidad de eventos: ")
            v = crear_arreglo(n)
            print("Arreglo creado!")
        if len(v) > 0:
            if op == 2:
                mostrar_arreglo(v)
            elif op == 3:
                p = validar_mayor(0, "Ingresar monto a comparar: ")
                generar_archivo(fd, v, p)
            elif op == 6:
                cod = input("Ingresar codigo")
                descripcion = busqueda_binaria(v, cod)
                if descripcion == -1:
                    print("No existe")

            elif op == 7:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
            elif op == 8:
                if descripcion != -1:
                    procesar_caracteres(descripcion)
                else:
                    print("No existe")
            elif op == 9:
                v2 = vector_conteo(v)
                mostrar_vector_conteo(v2)
        if op == 4:
            mostrar_archivo(fd)
        elif op == 5:
            v2 = arreglo_montos_produccion(fd)
            mostrar_arreglo(v2)
            prom = calcular_prom(v2)
            print("Promedio de montos: ", prom)



if __name__ == "__main__":
    main()