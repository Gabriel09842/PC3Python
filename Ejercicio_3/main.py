from area_circulo import circulo

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    circ1 = circulo(radio)
    area = circ1.calcular_area()
    print("El área del círculo es:", area)

if __name__ == "__main__":
    main()
