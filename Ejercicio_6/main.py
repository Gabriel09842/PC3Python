from producto import Producto, Catalogo

def main():
    catalogo = Catalogo()
    catalogo.agregar_producto(Producto("Llanta", "001", 100, 2022))
    catalogo.agregar_producto(Producto("Filtro de aceite", "002", 15, 2023))
    catalogo.agregar_producto(Producto("Batería", "003", 150, 2022))
    catalogo.mostrar_productos()
    catalogo.filtrar_por_año(2022)

if __name__ == "__main__":
    main()