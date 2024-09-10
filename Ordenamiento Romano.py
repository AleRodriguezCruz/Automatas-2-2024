#Ordenanmiento Romano
#Elaborado por: Alejandra Rodriguez de la Cruz 

# Definir la funcion que verifique que un caracter es un nuemro romano 


# Lista de palabras a desmenuzar
palabras = ["PIXEL", "PACO", "CIEN", "HIJO", "PASA", "CIVIL"]

# Caracteres válidos de números romanos y sus valores
valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'M': 1000}

# Función para verificar y convertir una secuencia de caracteres romanos a su valor numérico
def convertir_a_numero_romano(secuencia):
    total = 0
    valor_previo = 0
    repeticiones = 1

    for i in range(len(secuencia)):
        valor_actual = valores_romanos[secuencia[i]]
        
        # Verificar repeticiones y secuencias no válidas
        if i > 0 and secuencia[i] == secuencia[i - 1]:
            repeticiones += 1
            if repeticiones > 3:
                return None  # Más de 3 repeticiones no es válido
        else:
            repeticiones = 1
        
        # Comprobar secuencias inválidas como "IXI" y "IVI"
        if i > 1 and (secuencia[i-1] == 'I' and secuencia[i] == 'X' and secuencia[i-2] == 'I'):
            return None  # "IXI" no es válido
        elif i > 1 and (secuencia[i-1] == 'I' and secuencia[i] == 'V' and secuencia[i-2] == 'I'):
            return None  # "IVI" no es válido
        
        # Verificar si se debe restar
        if i > 0 and valor_previo < valor_actual:
            if not ((valor_previo == 1 and valor_actual in [5, 10]) or 
                    (valor_previo == 10 and valor_actual in [50, 100]) or 
                    (valor_previo == 100 and valor_actual in [500, 1000])):
                return None  # Resta no válida
            total += valor_actual - 2 * valor_previo  # Ajustar total
        else:
            total += valor_actual
        
        valor_previo = valor_actual
    
    return total

# Función para limpiar la secuencia y dejar solo números romanos válidos
def limpiar_secuencia(secuencia):
    secuencia_limpia = ""
    i = 0
    while i < len(secuencia):
        if i + 2 < len(secuencia) and secuencia[i:i+3] == "CIV":
            secuencia_limpia += "CIV"
            i += 3
            # Verificar si hay una 'I' adicional después de 'CIV'
            if i < len(secuencia) and secuencia[i] == 'I':
                i += 1
        elif i + 1 < len(secuencia) and secuencia[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            secuencia_limpia += secuencia[i:i+2]
            i += 2
        elif secuencia[i] in valores_romanos:  # Solo agregar caracteres válidos
            secuencia_limpia += secuencia[i]
            i += 1
        else:
            i += 1  # Saltar caracteres no válidos
    
    return secuencia_limpia

# Lista para almacenar los resultados
resultados = []

# Procesar cada palabra en la lista
for palabra in palabras:
    # Extraer caracteres válidos de la palabra
    extraidos = [char for char in palabra if char in valores_romanos]
    resultado = ''.join(extraidos)
    
    # Limpiar secuencia para eliminar combinaciones no válidas
    secuencia_limpia = limpiar_secuencia(resultado)
    
    # Asegurarse de que la secuencia limpia no esté vacía
    if secuencia_limpia:
        valor_numerico = convertir_a_numero_romano(secuencia_limpia)
        if valor_numerico is not None:
            resultados.append((palabra, secuencia_limpia, valor_numerico))
        else:
            print(f"Palabra original: {palabra} -> Caracteres válidos extraídos: {resultado} -> Secuencia no válida")
    else:
        print(f"Palabra original: {palabra} -> No se encontraron caracteres válidos")

# Ordenar los resultados de menor a mayor por el valor numérico
resultados.sort(key=lambda x: x[2])

# Imprimir los resultados ordenados
for palabra, secuencia, valor in resultados:
    print(f"Palabra original: {palabra} -> Caracteres válidos extraídos: {secuencia} -> Valor en número romano: {valor}")




