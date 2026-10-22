def contar_frecuencias(ruta):
    """
    Lee un archivo de texto y devuelve un diccionario con la
    frecuencia de cada palabra.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """

    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    palabras = texto.lower().split()

    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias

from pathlib import Path

def main():
    ruta = Path(__file__).parent / "texto.txt"
    print("Buscando en:", ruta)
    frecuencias = contar_frecuencias(ruta)

    print(f"Cantidad de palabras totales: {sum(frecuencias.values())}")
    print(f"Cantidad de palabras distintas: {len(frecuencias)}")
    print("\nLas 10 palabras mas frecuentes:")

    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top10:
        print(f"  {palabra}: {frecuencia}")

if __name__ == "__main__":
    main()
    