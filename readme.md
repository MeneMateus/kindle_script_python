# Script de Processamento de Destaques de Livros

Este script Python processa um arquivo de destaques de livros no formato TXT e cria arquivos Markdown separados para cada livro, contendo os destaques organizados por título.

## Como funciona

1. **Processamento do arquivo de destaques**: O script lê o arquivo TXT fornecido como entrada. Cada linha do arquivo é processada para extrair o título do livro e suas notas correspondentes. As notas são associadas ao título do livro encontrado anteriormente.

2. **Criação de arquivos Markdown**: Com base nos dados processados, o script cria arquivos Markdown separados para cada livro. Cada arquivo Markdown contém o título do livro e suas notas formatadas.

## Requisitos

- Python 3.x

## Como usar

1. **Instalação**: Certifique-se de ter o Python instalado em seu sistema.

2. **Clone o repositório**: Clone este repositório em seu sistema local.

3. **Execute o script**: Execute o script Python `script.py`, fornecendo o caminho para o arquivo de destaques de livros como argumento. Por exemplo:

    ```bash
    python3 script.py destaques.txt
    ```

    Isso processará o arquivo `destaques.txt` e criará arquivos Markdown correspondentes para cada livro.

4. **Verifique os arquivos Markdown gerados**: Após a execução do script, verifique a pasta de saída especificada (ou a pasta padrão "output") para encontrar os arquivos Markdown criados para cada livro.

## Argumentos opcionais

- `--output-dir`: Especifica o diretório de saída para os arquivos Markdown. Por padrão, os arquivos são salvos na pasta "output".

## Exemplo de arquivo de destaques de livros

Um exemplo do formato esperado do arquivo de destaques de livros é fornecido abaixo:

