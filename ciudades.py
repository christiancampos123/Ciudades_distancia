def rellenarMatriz():
    matriz = [[0] * 7 for _ in range(7)]
    try:
        fichero = open("C:/Users/christian.campos/Desktop/scripts de python/Ciudades/ciudades.txt", "r", encoding='utf-8')

    except:
        print("No ha funcionado")
    contador=0
    for linea in fichero:
        palabras = linea.split()
        matriz[contador]=palabras
        contador = contador+1

    fichero.close()

    return matriz

def obtenerCiudades():
    ciudades = input("Indique las ciudades separadas por espacio:   ")
    cadena=ciudades.split()
    ciudad1=cadena[0].lower()
    ciudad2=cadena[1].lower()
    return ciudad1, ciudad2

def compararDistancias():
    ciudad1, ciudad2 = obtenerCiudades()
    print("la distancia entre ", ciudad1,"y",ciudad2, "es: ")

    col=0
    try:
        for _ in matriz:
            if matriz[0][col].lower()==ciudad1:
                colBuena = col
            col += 1
    except:
        print("no funciono")
    fil = 0
    try:
        for _ in matriz:
            if matriz[0][fil].lower()==ciudad2:
                filBuena = fil
            fil += 1
    except:
        print("no funciono")
    
    try:
        if (matriz[colBuena][filBuena] == "x"):
            print(matriz[filBuena][colBuena], "KM",'''
            ''')
        else:
            print(matriz[colBuena][filBuena], "KM",'''
            ''')
    except:
        print("No se han encontrado las ciudades")

matriz=rellenarMatriz()
compararDistancias()