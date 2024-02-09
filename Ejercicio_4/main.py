from area_rectangulo import rectangulo

def main():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rect1 = rectangulo(largo, ancho)
    area = rect1.calcular_area()
    print("El área del rectángulo es:", area)

if __name__ == "__main__":
    main()
