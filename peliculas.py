import funciones
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR CARACTERISTICA A UNA PELICULA ::::...\n")
    caracteristica=input("Ingresa la caracteristicas: ").upper().strip()

    pelis.append(peli)
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR  CARACTERISTICA DE LA PELICULA ::::...\n")
    if len (pelis)>0:
        print("\tCaracteristica\t\valor")
        for i in
        print(f"\t(i)\t\t{pelis[i]}")
    funciones.espereTecla()
   
def limpiarPeliculas(pelis):
     print("\t\t....:::: BORRRAS TODAS  CARATERISTICAS DE LA PELICULAS ::::...\n") 
     if len(pelis)>0:
         opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
         if opc=="si":
             pelis=pelis.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen peliculas que borrar, verifique! ....")
    
def buscarPeliculas(pelis):
    print("\t\t....:::: BUSCAR CARACTERISCA DE LA PELICULA ::::...\n")   
    caracterisca=input("Escribe la caracterisca de la pelicula: ").upper().strip()
    print("\tcaracteristica\t\valor")
    noencroto=False
    for i in pelis:
      if caracterisca==i:
        print(f"\t{i}\t\t{pelis[i]}")
        noencroto=True
    funciones.espereTecla()
    if not(noencroto):
       input("\n\t...¡NO existe esta carateristica no exitec")


def borrarPeliculas(pelis):
    posiciones=[]
    print("\t\t....:::: BORRAR  CARACTERISTICA PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la Caracteristicas: ").upper().strip()
    noencontro=False
    for i in pelis:
     if caracteristicas==i:
      opc=""
      while opc!="si" and opc!="no":
        opc=input("¿Deseas borrar la caracteristicas (Si/No)? ").lower().strip()
     if opc=="si":
      pelis.pop(caracteristica )
     funciones.accionExitosa()
     noencontro=False
    if noencontro:
      input("\n\t...¡No existe la pelicula que andas buscando!...")

def modificarPeliculas(pelis):
    print("\t\t....:::: MODIFICAR LAS CARACTERISTICAS PELICULAS ::::...\n")   
    peli=input("Escribe el nombre de la  Caracteristicas: ").upper().strip()
    noencontro=True
    if peli in pelis:
            if caracteristica== 1:
              opc=""
              while opc!="si" and opc!="no":
                opc=input("¿Deseas mofificar la caracteriscas (Si/No)? ").lower().strip()
              if opc=="si":
                pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("\n\t...¡No existe la caracteriscas andas buscando!...")
 

def buscarpeliculas2(pelis)
    print("\t\t....::::buscar caracteristicas de la peliculas ::::....\n")
    caracteriscas=input("Escribe el nombre de la caracteristica: "). upper().strip()
    
    noencontro=True
    for i in pelis:
     if caracteriscas==i:
      print("\tCaracteristicas\Valor")
      print(f"\t(i)\t\{pelis(i)}")
     noencontro=False
     funciones.espereTecla()
    if nocecontro:
       inpur("\n\t...¡NO existe esta caracterisca que andas buscando!...")

