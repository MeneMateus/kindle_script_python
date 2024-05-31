import argparse
import os

def process_file(file_path):
    books = {}
    current_title = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue  # Ignorar linhas em branco

            print(f"Linha {line_num}: {line}")

            # Se a linha começa com o título do livro, definir o título atual
            if "Z-Library" in line:
                current_title = line.split("Z-Library")[0].strip()
                if current_title not in books:
                    books[current_title] = {"notas": []}
                print(f"Título encontrado: {current_title}")
            # Caso contrário, assumir que é uma nota e adicionar ao título atual
            elif current_title:
                # Substituir '========' por quebras de linha
                if line == "=" * len(line):
                    books[current_title]["notas"].append("\n")
                else:
                    # Adicionar formatação de citação à nota
                    books[current_title]["notas"].append(f"> {line}")
                print(f"Nota adicionada para '{current_title}': {line}")

    return books

def save_as_markdown(books, output_dir):
    # Criar diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Salvar cada livro como um arquivo Markdown
    for title, details in books.items():
        # Substituir caracteres inválidos nos nomes de arquivos
        safe_title = title.replace('/', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').strip()
        
        # Criar o nome do arquivo Markdown
        filename = os.path.join(output_dir, f"{safe_title}.md")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"# Título: {title}\n\n")
            file.write("Notas:\n\n")
            for note in details["notas"]:
                file.write(f"{note}\n")
            print(f"Arquivo '{filename}' criado com sucesso.")

def main():
    parser = argparse.ArgumentParser(description="Processa um arquivo de destaques de livros e cria arquivos Markdown para cada livro.")
    parser.add_argument('file_path', type=str, help='Caminho para o arquivo de destaques em formato TXT')
    parser.add_argument('--output-dir', type=str, default='output', help='Diretório de saída para os arquivos Markdown (padrão: "output")')
    args = parser.parse_args()

    print(f"Processando arquivo: {args.file_path}")
    books = process_file(args.file_path)
    print("Processamento concluído.")

    print("Salvando arquivos Markdown:")
    save_as_markdown(books, args.output_dir)
    print("Concluído.")

if __name__ == "__main__":
    main()
