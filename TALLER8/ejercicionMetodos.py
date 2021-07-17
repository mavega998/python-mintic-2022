def menu():
    bandera = True
    palabra = "programacion"
    pSoftware = "software"
    pProgramas = "programas"
    cadena = "Sin un {} adecuado, la computadora de nada servirá. Dentro del software se incluyen {} informáticos comunes como Word, Excel o PowerPoint, también navegadores como Chrome y Mozilla Firefox y sistemas operativos como Microsoft Windows o MacOS"
    while bandera:
        try:
            print("---- Menú de ejecución ----")
            print("1. Mostrar programación capitalizada.\n" +
            "2. Buscar letra e dentro de cadena.\n" +
            "3. Contar caracteres de cadena.\n" +
            "4. Buscar palabra 'Chrome' en cadena.\n"+
            "5. Formatear cadena.\n" +
            "6. Remplazar 'Word' por 'Publisher'")
            opcion = int(input("\nIngrese opcion (Para salir ingrese 0): "))
            if opcion == 0:
                bandera = False
                print("Saliendo...")
            elif opcion == 1:
                pCapitalizada = capitalizar(palabra)
                print("Se capitalizó", palabra, "por", pCapitalizada,".\n")
            elif opcion == 2:
                nuevaCadena = formatearCadena(cadena, pSoftware, pProgramas)
                countLetra = contarLetra('e', nuevaCadena)
                print("La letra e se repite",countLetra,"veces.\n")
            elif opcion == 3:
                nuevaCadena = formatearCadena(cadena, pSoftware, pProgramas)
                cantidadCaracter = longitudCadena(nuevaCadena)
                print("El tamaño de la cadena es de", cantidadCaracter,".\n")
            elif opcion == 4:
                nuevaCadena = formatearCadena(cadena, pSoftware, pProgramas)
                posicion = buscar('Chrome', nuevaCadena)
                print("La palabra 'Chrome' se encuentra en la posición", posicion, "de la cadena.\n")
            elif opcion == 5:
                nuevaCadena = formatearCadena(cadena, pSoftware, pProgramas)
                print(nuevaCadena,"\n");
            elif opcion == 6:
                nuevaCadena = formatearCadena(cadena, pSoftware, pProgramas)
                cReemplazada = reemplazar(nuevaCadena, "Word", "Publisher")
                print(cReemplazada,"\n")
            else:
                print("La opción no es válida.\n")
        except ValueError:
            print("La opción no es válida.\n")


def capitalizar(palabra):
    return palabra.capitalize()

def contarLetra(letra, cadena):
    return cadena.count(letra) 

def longitudCadena(cadena):
    return len(cadena)

def formatearCadena(cadena, palabra1, palabra2):
    return cadena.format(palabra1, palabra2)

def buscar(palabra, cadena):
    return cadena.find(palabra)

def reemplazar(cadena, palabraExistente, palabraNueva):
    return cadena.replace(palabraExistente, palabraNueva)

menu()