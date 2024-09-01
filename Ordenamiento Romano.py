#Ordenanmiento Romano
#Elaborado por: Alejandra Rodriguez de la Cruz 

# Definir la funcion que verifique que un caracter es un nuemro romano 

def es_numero_romano(caracter):
    caracteres_romanos = "IVXLCDM"
    return caracter.upper() in caracteres_romanos


# Definir la funcion para obtener el valor romano 
def obtener_valor_romano(caracter):
    # Creamos un diccionario que asigna los valores a los numeros romanos
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return valores_romanos.get(caracter.upper(), 0)

# Definimos la funcion que calcula la suma de numeros romanos en una palabra
def calcular_suma_numeros_romanos(palabra):
    suma_total = 0
    for caracter in palabra:
        suma_total += obtener_valor_romano(caracter)
    return suma_total

# Definimos funcion principal

def main():
    palabras = ["miel", "pixel", "cima", "ximana", "hijo", "PASA", "ale"]

    suma_palabras = [(palabra, calcular_suma_numeros_romanos(palabra))for
palabra in palabras]
    
    suma_palabras.sort(key=lambda x: x[1])

    print("Palabras ordenadas por la suma de sus valores en numeros romanos")
    for palabra, suma in suma_palabras:
        print(f"{palabra}: {suma}")

# Ejecutamos la funcion principal
if __name__ =="__main__" :
    main()




