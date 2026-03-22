import os
import re

def extrair_numero(nome_arquivo):
    # Procura por números no nome do arquivo para garantir a ordem 1, 2, 3...
    numeros = re.findall(r'\d+', nome_arquivo)
    return int(numeros[0]) if numeros else 0

def concatenar_csvs(diretorio_origem, arquivo_saida):
    # 1. Lista apenas arquivos .csv e ignora o arquivo de saída se ele já existir
    arquivos = [f for f in os.listdir(diretorio_origem) 
                if f.endswith('.csv') and f != arquivo_saida]
    
    # 2. Ordenação Natural (Garante que o Cap 2 venha antes do Cap 10)
    arquivos.sort(key=extrair_numero)
    
    print(f"Arquivos encontrados na ordem: {arquivos}")

    with open(arquivo_saida, 'w', encoding='utf-8') as destino:
        for i, nome_f in enumerate(arquivos):
            caminho_completo = os.path.join(diretorio_origem, nome_f)
            
            with open(caminho_completo, 'r', encoding='utf-8') as origem:
                conteudo = origem.read().strip()
                
                # 3. Adiciona uma quebra de linha apenas se o arquivo não estiver vazio
                if conteudo:
                    destino.write(conteudo + '\n')
            
            print(f"[{i+1}/{len(arquivos)}] {nome_f} mesclado com sucesso.")


# O caminho da pasta onde estão os arquivos csv
pasta_dos_capitulos = './Biblia/Capitulos' 
nome_do_final = '01_Genesis.csv'

concatenar_csvs(pasta_dos_capitulos, nome_do_final)