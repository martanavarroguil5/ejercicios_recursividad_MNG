# La entrada es una cadena de caracteres, los cuales deben cumplir 3 prereqisitos (precondiciones).
# 1. Que tenga unos caracteres permitidos
# 2. Que no tenga mayusuculas
# 3. N o debe haber mayúsuclas

# Primero filtramos aquellos caracteres que no nos interesan. 
# Creamos una nueva cadena que incorpore solo aquellos caracyeres que conideramos válidos
def filtrar_caracteres(texto):
    caracteres_permitidos = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ÁÉÍÓÚáéíóú'
    texto_filtrado = ''.join(caracter for caracter in texto if caracter in caracteres_permitidos)
    return texto_filtrado

# Para eliminar acentos esta función  intercambia el caracter con acento por el caracter sin acento.
def quitar_acentos(texto):
    caracteres_con_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    texto_sin_acentos = ''.join(caracter 
                                if caracter not in caracteres_con_acentos 
                                else caracteres_con_acentos[caracter] 
                                for caracter in texto)
    return texto_sin_acentos

# Convertir los caracteres en minúsculas
def convertir_a_minusculas(texto):
    texto_en_minusculas = texto.lower()
    return texto_en_minusculas

# Función recursiva que evalúa si se trata de un palíndromo una vez modificado el texto
def es_palindromo(texto):

    # Función auxiliar para verificar si un texto es palíndromo de forma recursiva
    def es_palindromo_aux(texto_filtrado):

        #Si la longitud del texto es 0 o 1 automaticamente es palíndromo.
        if len(texto_filtrado) <= 1:
            return True
        
        # Verifica si el primer y último carácter son iguales y llama recursivamente a la función. 
        # con el texto truncado
        else:
            return texto_filtrado[0] == texto_filtrado[-1] and es_palindromo_aux(texto_filtrado[1:-1])

    texto_filtrado = filtrar_caracteres(texto)
    texto_sin_acentos = quitar_acentos(texto_filtrado)
    texto_en_minusculas = convertir_a_minusculas(texto_sin_acentos)
    return es_palindromo_aux(texto_en_minusculas) # La salida es un booleano


# Ejemplo de uso:
ejemplos = [
    "Dábale arroz a la zorra el abad",
    "Logré ver gol",
    "Salas",
    "1754571",
    "10000000000000000001",
    "Oso",
    "¡Anita, lava la tina!",
    "A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá.",
    "A torre da derrota.",
]

for ejemplo in ejemplos:
    if es_palindromo(ejemplo):
        print(f'"{ejemplo}" es un palíndromo.')
    else:
        print(f'"{ejemplo}" no es un palíndromo.')
