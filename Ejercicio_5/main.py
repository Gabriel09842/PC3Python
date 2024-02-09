from alumno import Alumno

def main():
    alumno1 = Alumno("Juan", "A12345")
    alumno1.setAge(20)
    alumno1.setNotas([12, 18, 17])
    alumno1.Display()
pass

if __name__ == "__main__":
    main()

