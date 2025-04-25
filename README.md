# PDF Merger

Este projeto é um script de automação que permite unir múltiplos arquivos PDF em um único documento de forma prática e rápida.

## Funcionalidades

- Mescla vários arquivos PDF em um único arquivo.
- Ordena os PDFs automaticamente antes de unir.
- Facilita a organização e a consolidação de documentos.

## Tecnologias utilizadas

- Python 3
- Biblioteca `PyPDF2`
- Biblioteca `os` (nativa do Python)

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/c4rl0sfilho/UnificadorPDFs.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd nome-da-pasta
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install PyPDF2
   ```

4. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate  # No Windows
   source venv/bin/activate # No Mac/Linux
   ```

5. Organize seus arquivos PDF dentro da pasta especificada (`MergePDFs/files`) e execute o script:
   ```bash
   python pdf_merger.py
   ```

6. O arquivo final será salvo com o nome `merged_output.pdf` na pasta `MergePDFs`.

## Créditos

Projeto inspirado pelas aulas do canal **Hashtag Programação** no YouTube.
