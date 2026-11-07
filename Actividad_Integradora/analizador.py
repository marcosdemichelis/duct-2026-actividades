import matplotlib.pyplot as plt

def leer_archivo(ruta):
    """
    Intenta abrir y leer un archivo de texto.
    Devuelve el contenido como string si existe, o None si no se encuentra.

    Parámetros:
    ruta (str): Ruta relativa o absoluta del archivo de texto.

    Retorna:
    str | None: El contenido completo del archivo si existe, o None si no se encuentra.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return None

def contar_frecuencias(texto):
    """
    Recibe el string de texto y devuelve un diccionario con la frecuencia
    de cada palabra en minúsculas.

    Parámetros: 
    texto (str): Cadena de texto a procesar.

    Retorna: 
    dict: Diccionario con pares {palabra: frecuencia}
    """
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def generar_grafico(frecuencias, top_n=10):
    """
    Recibe el diccionario de frecuencias y guarda un gráfico de barras horizontales
    con las top_n palabras más frecuentes.

    Parámetros:
    frecuencias (dict): Diccionario con pares {palabra: frecuencia}
    top_n (int): Número de palabras más frecuentes a mostrar en el gráfico.
    
    Retorna:
    None
    """
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    palabras = [palabra for palabra, _ in top10]
    valores = [valor for _, valor in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()

def main():
    """
    Abre el archivo de texto, cuenta las frecuencias 
    de palabras y genera un gráfico de barras. 
    Si no encuentra el archivo, termina la ejecución.
    """
    texto = leer_archivo("texto_integradora.txt")
    if texto is None:
        return

    frecuencias = contar_frecuencias(texto)
    generar_grafico(frecuencias, top_n=10)

if __name__ == "__main__":
    main()