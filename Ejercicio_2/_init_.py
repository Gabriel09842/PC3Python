from calificacion import procesar_calificaciones

def main():
    while True:
        cadena_calificaciones = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones = procesar_calificaciones(cadena_calificaciones)
        if calificaciones is not None:
            print("Calificaciones procesadas:", calificaciones)
            break

if __name__ == "__main__":
    main()
