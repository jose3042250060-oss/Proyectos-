def borrarPantalla():
    print("\033c")
    
def espereTecla():
    input("...¡Oprima cualquier tecla para contunuar!...")
    
def accionExitosa():
    input("...¡Accion Realizada con Exito!...")
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion

def terminarSistema():
    input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")
    
def opcionInvalida():
    input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ")   
    
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Ingresa la pelicula: ").upper().strip()
    pelis.append(peli)
    accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR PELICULAS ::::...\n")
    print("\tCódigo\t\tPelícula")
    for i in range(0,len(pelis)):
        print(f"\t{i+1}\t\t{pelis[i]}")
    espereTecla()

def limpiarPeliculas(pelis):
    print("\t\t....:::: BORRRAS TODAS PELICULAS ::::...\n") 
    if len(pelis)>0:
        opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
        while opc!="si" and opc!="no":
            opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
        if opc=="si":
            pelis=pelis.clear()
            accionExitosa()
    else:
        input("\n\t...¡No existen peliculas que borrar, verifique! ....")
    
def buscarPeliculas(pelis):
    print("\t\t....:::: BUSCAR PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        print("\tCódigo\t\tPelícula")
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
                print(f"\t{i+1}\t\t{pelis[i]}")
        espereTecla()
    else:
        input("\n\t...¡No existe la pelicula que andas buscando!...")

def borrarPeliculas(pelis):
    print("\t\t....:::: BORRAR PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la pelicula: ").upper().strip()
    if peli in pelis:
        print("\tCódigo\t\tPelícula")
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
                opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
                while opc!="si" and opc!="no":
                        opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                    pelis.remove(peli)
                    accionExitosa()
                espereTecla()
    else:
        input("\n\t...¡No existe la pelicula que andas buscando!...")

