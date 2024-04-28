#La entrada es una tabla y una componente que hay que encntrar su posicion en dicha tabla.

# Función que encuentra la posicion de dicho elemeneto en la tabla mediante recursividad
def dicotomia_recursiva(t, c):
    def buscar(izquierda, derecha):
        if izquierda > derecha:
            return -1  # Si no se encuentra el elemento, devuelve -1
        
        medio = (izquierda + derecha) // 2
        if t[medio] == c:
            return medio  # Si encontramos el elemento, retornar su índice
        elif t[medio] < c:
            return buscar(medio + 1, derecha)  # Buscar en la mitad derecha
        else:
            return buscar(izquierda, medio - 1)  # Buscar en la mitad izquierda
    
    # Llamar a la función auxiliar con los índices iniciales de la tabla
    return buscar(0, len(t) - 1) # Salida: la posición (int)

# Ejemplo de uso
tabla = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
componente = 12
posicion = dicotomia_recursiva(tabla, componente)
if posicion != -1:
    print(f"El elemento {componente} se encuentra en la posición {posicion}.")
else:
    print(f"El elemento {componente} no se encuentra en la tabla.")
