#Ordenanmiento Romano
#Elaborado por: Alejandra Rodriguez de la Cruz 

# Definir la funcion que verifique que un caracter es un nuemro romano 


def es_numero_romano_valido(cadena_romana):
    # Definición de combinaciones válidas
    combinaciones_validas = {
        "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
        "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
        "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
        "M", "MM", "MMM", "CIV", "CMI", "MCM", "MCD", "MD", "MDL"
    }
    return cadena_romana in combinaciones_validas

def romano_a_decimal(cadena_romana):
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    valor_previo = 0
    
    for caracter in reversed(cadena_romana):
        valor = valores_romanos[caracter]
        if valor < valor_previo:
            total -= valor
        else:
            total += valor
        valor_previo = valor
    
    return total

def encontrar_numero_romano_mayor(cadena_romana):
    numero_romano_mayor = ''

    # Iterar sobre cada carácter en la cadena
    for i in range(len(cadena_romana)):
        for j in range(i + 1, len(cadena_romana) + 1):
            # Obtener la combinación actual
            combinacion_actual = cadena_romana[i:j]
            
            # Verificar si la combinación actual es válida
            if es_numero_romano_valido(combinacion_actual):
                # Actualizar el mayor número romano si es más grande
                if len(combinacion_actual) > len(numero_romano_mayor):
                    numero_romano_mayor = combinacion_actual

    return numero_romano_mayor

def extraer_caracteres_romanos(palabra):
    caracteres_romanos = ''
    for caracter in palabra:
        if caracter in 'IVXLCDM':
            caracteres_romanos += caracter
    return caracteres_romanos

# Ejemplo de uso
palabras = ["PIXEL", "CIVIL", "PACO", "ALE", "CAMIÓN", "HIJO"]

numeros_romanos = []
for palabra in palabras:
    cadena_romana = extraer_caracteres_romanos(palabra)
    numero_romano_mayor = encontrar_numero_romano_mayor(cadena_romana)
    if numero_romano_mayor:  # Asegurarse de que no esté vacío
        valor_decimal = romano_a_decimal(numero_romano_mayor)
        numeros_romanos.append((palabra, numero_romano_mayor, valor_decimal))

# Ordenar de menor a mayor por valor decimal
numeros_romanos.sort(key=lambda x: x[2])

print("Palabras, números romanos y sus valores ordenados de menor a mayor:")
for palabra, numero_romano, valor_decimal in numeros_romanos:
    print(f"{palabra} -> {numero_romano} -> {valor_decimal}")
