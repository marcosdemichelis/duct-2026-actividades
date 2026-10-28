import matplotlib.pyplot as plt
import spacy

nlp = spacy.load("es_core_news_sm")

def analizar_y_graficar(ruta, top_n=20):
    """
    Lee un archivo de texto, cuenta la frecuencia de cada palabra
    y genera un grafico de barras horizontales con las top_n
    palabras mas frecuentes.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar
        top_n (int): cantidad de palabras a graficar

    Retorna:
        None (genera y guarda el grafico)
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    doc = nlp(texto)
    palabras_texto = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

    frecuencias = {}
    for palabra in palabras_texto:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    palabras = [palabra for palabra, frecuencia in top10]
    valores = [frecuencia for palabra, frecuencia in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()

def main():
    analizar_y_graficar("texto.txt")

if __name__ == "__main__":
    main()