import os

Libros_prestados = []
titulos = ["el alquimista", "el hombre mas rico de babilonia", "el metodo"]

def registro():
    try:

        ntitulo = ntitulo = input("Ingrese el título del libro: ") #ntitulo = nombre del titulo
        autor = input("Ingrese el nombre del autor del libro: ")
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        añopublicación = int(input("Ingrese el año de publicación: "))
        SKU = input("Ingrese el SKU: ") 

        if nombre_usuario == "" or SKU == "" or ntitulo == "" or autor == "" or añopublicación <=0:
           print("Faltaron datos por ingresar")
        else:
            
            prestamo = {
                'Nombre del usuario' : nombre_usuario,
                'SKU' : SKU,
                'Nombre del titulo' : ntitulo,
                'Autor' : autor,
                'Año de publicación' : añopublicación
            }
            Libros_prestados.append(prestamo)
            print ("Registro se realizo exitosamente")
    except ValueError:
        print ("Dato erroneo. Intente nuevamente")

def listar ():
    print("prestamo\t\tSKU\t\tNombre del titulo\t\tAutor\t\tAño de publicación\n")
    for prestamo in Libros_prestados:
        print(f"{prestamo[ 'Nombre del usuario' ]}\t\t{prestamo['SKU']}\t\t{prestamo['Nombre del título']}\t\t{prestamo['Autor']}\t\t{prestamo['Año de publicación']}")

def imprimir():
    try:
        op = int(input("¿Como desea imprimir la planilla?\n1.Todos\n2.SKU específico\nOpción: "))
        if op == 1:
            with open ('planilla_libros.txt', 'w') as archivo:
                archivo.write("Nombre del título\t\tAutor\t\t\t\tAño Publicación\t\tSKU\n")
                for prestamo in Libros_prestados:
                    archivo.write(f"{prestamo['Nombre del usuario']}\t\t{prestamo['SKU']}\t\t{prestamo['Autor']}\t\t{prestamo['Año de publicación']}")
            print("Planilla generada exitosamente en: ",os.getcwd())
        elif op == 2:
            SKU  = input("Ingrese el nombre del titulo: ").lower()
            if not SKU in titulos:
                print("Libro no existe o Libro ya prestado")
            else:
                with open(f'planilla_{SKU}.txt', 'w') as archivo:
                    archivo.write("Nombre del título\t\tAutor\t\t\t\tAño Publicación\t\tSKU\n")
                    for prestamo in Libros_prestados:
                        if prestamo['SKU'].lower() ==SKU:
                            archivo.write(f"{prestamo['Nombre del usuario']}\t\t{prestamo['SKU']}\t\t{prestamo['Nombre del título']}\t\t{prestamo['Autor']}\t\t{prestamo['Año de publicación']}")
                print("Planilla generada exitosamente en: ",os.getcwd())


    except ValueError:
        print("Dato Erroneo. Inntente nuevamente")
def menu():
    while True:
        try:
            print("***MENU***")
            print("1.Registro de usuario\n2.Lista de usuarios\n3.Imprimir planilla\n4.Salir")
            op = int(input("Ingrese una opción: "))
        except ValueError:
            print("Dato erroneo. Intente nuevamente")
        if op == 1:
            registro()
        elif op ==2:
            listar()
        elif op ==3:
            imprimir()
        elif op ==4:
            print("Programa finalizado...")
            print("Desarrollado por Kevin Castillo")
            print("Run: 20.814.556-8")
            break
        else:
            print("La opción ingresada esta fuera de rango, por favor intente nuevamente")            
        

        

     
        
          

