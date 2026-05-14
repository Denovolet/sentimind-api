const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.get('/analisar', (req, res) => {
    const textoParaAnalisar = req.query.texto || "Estou muito feliz com este projeto";
    
    // Aqui o Node chama o Python "na mão"
const pythonProcess = spawn('python3', ['analyzer.py', textoParaAnalisar]);
    let resultado = "";

    pythonProcess.stdout.on('data', (data) => {
        resultado += data.toString();
    });

    pythonProcess.on('close', (code) => {
        res.json({
            status: "sucesso",
            input: textoParaAnalisar,
            sentimento: resultado.trim(),
            engine: "Python 3 (TextBlob)"
        });
    });
});

app.listen(port, () => {
    console.log(`🚀 Servidor rodando em http://localhost:${port}`);
});
