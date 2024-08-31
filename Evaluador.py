def es_caracter_valido(caracter):
    return caracter in [34, 44, 58, 32] or (caracter >= 48 and caracter <= 57) or (caracter >= 65 and caracter <= 90) or (caracter >= 97 and caracter <= 122)

def tokenizar_cadena(tokens):
    tokens_agrupados = []
    for token in tokens:
        if es_caracter_valido(token):
            tokens_agrupados.append(token)
        else:
            tokens_agrupados.append(888)  # Token para caracteres no válidos
    return tokens_agrupados

def mostrar_contenido_tokens(contenido, tokens, tokens_agrupados):
    for i in range(len(tokens)):
        if tokens_agrupados[i] == 34:
            print(f'"{contenido[i]}"= Texto')
        elif tokens_agrupados[i] == 44:
            print(f',{contenido[i]}= Separador')
        elif tokens_agrupados[i] == 58:
            print(f':{contenido[i]}= Separador')
        elif tokens_agrupados[i] == 32:
            print(f'{contenido[i]}= Espacio en blanco')
        elif tokens_agrupados[i] >= 48 and tokens_agrupados[i] <= 57:
            print(f'{contenido[i]}= Número entero')
        elif tokens_agrupados[i] >= 65 and tokens_agrupados[i] <= 90:
            print(f'{contenido[i]}= Letra mayúscula')
        elif tokens_agrupados[i] >= 97 and tokens_agrupados[i] <= 122:
            print(f'{contenido[i]}= Letra minúscula')
        else:
            print(f'{contenido[i]}= Carácter no válido')

def main():
    contenido_archivo = [
        123, 10, 32, 32, 32, 32, 34, 110, 111, 109, 98, 114, 101, 34, 58, 32, 34, 97, 108, 101, 106, 97, 110, 100, 114, 97, 50, 34, 44, 10,
        32, 32, 32, 32, 34, 101, 110, 116, 101, 114, 111, 34, 58, 32, 51, 54, 44, 10, 32, 32, 32, 32, 34, 100, 101, 99, 105, 109, 97, 108, 34,
        58, 32, 49, 46, 53, 44, 10, 32, 32, 32, 32, 34, 102, 101, 99, 104, 97, 34, 58, 32, 49, 48, 45, 48, 53, 45, 50, 48, 50, 52, 10, 125
    ]
    tokens_originales = contenido_archivo
    tokens_agrupados = tokenizar_cadena(tokens_originales)
    
    mostrar_contenido_tokens(contenido_archivo, tokens_originales, tokens_agrupados)

if __name__ == '__main__':
    main()
