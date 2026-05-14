import sys
from textblob import TextBlob

def main():
    if len(sys.argv) > 1:
        texto = sys.argv[1]
        blob = TextBlob(texto)
        polaridade = blob.sentiment.polarity
        
        if polaridade > 0:
            print("Positivo")
        elif polaridade < 0:
            print("Negativo")
        else:
            print("Neutro")
    else:
        print("Nenhum texto fornecido.")

if __name__ == "__main__":
    main()
