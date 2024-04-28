# La entrada es una lista desordenada de fichas verdes, rojas y azules.

# Esta función ordena las ficha mediante recursividad
def ordenar_fichas(fichas):

    # Función recursiva para ordenar las fichas
    def ordenar_rec(fichas, inicio, fin, color):
        if inicio >= fin:
            return

        # Encuentra la primera posición de un color diferente al color actual
        while inicio < fin and fichas[inicio] == color:
            inicio += 1

        # Encuentra la última posición de un color diferente al color actual
        while inicio < fin and fichas[fin] != color:
            fin -= 1

        # Si las posiciones no se cruzan, intercambia las fichas
        if inicio < fin:
            fichas[inicio], fichas[fin] = fichas[fin], fichas[inicio]
            # Llama recursivamente para seguir ordenando
            ordenar_rec(fichas, inicio + 1, fin - 1, color)

    # Ordena las fichas rojas al principio
    ordenar_rec(fichas, 0, len(fichas) - 1, 'roja')
    # Ordena las fichas verdes en el centro
    ordenar_rec(fichas, 0, len(fichas) - 1, 'verde')
    # Ordena las fichas azules al final
    ordenar_rec(fichas, 0, len(fichas) - 1, 'azul')

# Ejemplo de uso
fichas = ['roja', 'azul', 'verde', 'roja', 'verde', 'azul', 'roja']
ordenar_fichas(fichas)
print(fichas) 

