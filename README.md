# Sentimind API | Node.js + Python Integration

Este projeto é uma API desenvolvida para demonstrar a integração entre **Node.js** e **Python**, utilizando o melhor de cada stack para processamento de linguagem natural (NLP).

##  Sobre o Projeto
A aplicação consiste em um servidor web que recebe textos via requisições HTTP e delega a lógica de análise de sentimentos para um script especializado em Python. É um exemplo prático de **interoperabilidade** e gerenciamento de processos assíncronos.

##  Tecnologias e Conceitos
- **Node.js + Express**: Responsável pelo roteamento da API e interface de entrada de dados.
- **Python 3**: Utilizado para o motor de processamento lógico da análise de texto.
- **Child Process (Spawn)**: Utilizado para comunicação assíncrona entre o servidor Node e o interpretador Python.
- **REST API**: Estrutura de endpoints para comunicação limpa e escalável.

##  Estrutura de Arquivos
- `server.js`: O servidor principal que gerencia o fluxo da aplicação.
- `analyzer.py`: O script Python que executa a lógica de classificação de sentimentos.
- `package.json`: Gerenciamento de dependências e metadados do projeto Node.

##  Como funciona
1. O usuário faz uma requisição para a rota `/analisar?texto=exemplo`.
2. O Node.js inicia um processo Python em background.
3. O script Python analisa as palavras-chave e retorna a polaridade (Positivo, Negativo ou Neutro).
4. O Node devolve um JSON estruturado para o cliente final.

---
Desenvolvido por **Letícia N. (Denovolet)** 
