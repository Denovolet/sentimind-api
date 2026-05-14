import sys

def analisar_sentimento(texto):
    positivas = ['feliz', 'amando', 'bom', 'otimo', 'maravilhoso', 'projeto', 'consegui']
    negativas = ['ruim', 'triste', 'pessimo', 'erro', 'odiei']
    
    texto_low = texto.lower()
    
    # Se encontrar qualquer palavra positiva
    if any(palavra in texto_low for palavra in positivas):
        return "Positivo"
    # Se encontrar qualquer palavra negativa
    elif any(palavra in texto_low for palavra in negativas):
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    # Pega o texto ignorando o primeiro argumento (nome do script)
    frase = " ".join(sys.argv[1:])
    print(analisar_sentimento(frase))
