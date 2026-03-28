import re
import csv

def salvar_para_csv(texto_bruto, sigla_livro, capitulo, nome_arquivo):
    # Limpa espaços e quebras de linha duplas
    texto_unificado = re.sub(r'\s+', ' ', texto_bruto).strip()

    # 1. Regex que identifica: [Número] [Espaço] [Letra Maiúscula]
    # Isso evita capturar números como "2 de cada espécie" no meio da frase como versiculo
    # padrao = r'(\d+)\s+([A-Z].+?)(?=\s+\d+\s+[A-Z]|$)'
    
    # 2. Regex aprimorado para aceitar letras acentuadas e minúsculas, além de garantir que 
    # o próximo número seja seguido por um espaço e uma letra maiúscula ou seja o fim do texto:
    # [a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ] -> Aceita qualquer letra (maiusc/minusc/acentuada)
    # (?=\s+\d+\s+|$) -> Para antes do próximo número ou fim do texto

    padrao = r'(\d+)\s+([a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\“\”\'\-\(].+?)(?=\s+\d+\s+|$)'

    versiculos = re.findall(padrao, texto_unificado)

    # Gravação física do arquivo CSV
    with open(nome_arquivo, mode='a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        # Se o arquivo estiver vazio, pode-se escrever o cabeçalho:
        # escritor.writerow(['Livro', 'Capitulo', 'Versiculo', 'Texto'])
        
        for num, texto in versiculos:
            escritor.writerow([sigla_livro, capitulo, num, texto.strip()])

    print(f"Sucesso! {len(versiculos)} versículos adicionados ao arquivo {nome_arquivo}.")

# Uso:
texto_puro = """1 O Senhor chamou Moisés e falou-lhe da tenda de reunião: 2 “Fala — 
oferta ao Senhor, será dentre o gado maior ou menor que oferecereis. 

3 Se a oferta for um holocausto tirado do gado maior, oferecerá um 
macho sem defeito; e o oferecerá à entrada da tenda de reunião para obter o 
favor do Senhor. 4 Porá a mão sobre a cabeça da vítima, que será aceita em 
seu favor para lhe servir de expiação. 5 Matará o novilho diante do Senhor. 
Os sacerdotes, filhos de Aarão, oferecerão o sangue e o derramarão ao redor 
sobre o altar que está à entrada da tenda de reunião. 6 Tirará a pele da vítima 
e esta será cortada em pedaços. 7 Os filhos do sacerdote Aarão porão fogo 
no altar e empilharão a lenha sobre ele, 8 dispondo, em seguida, por cima da 
lenha, os pedaços, a cabeça e a gordura. 9 Lavarão com água as entranhas e 
as pernas, e o sacerdote queimará tudo sobre o altar. Esse é um holocausto, 
um sacrifício consumido pelo fogo, de odor agradável ao Senhor. 

10 Se a sua oferta for um holocausto tirado do gado menor, dos cordeiros 
ou das cabras, oferecerá um macho sem defeito. 1 Matará o animal ao do 
lado norte do altar, diante do Senhor, e os sacerdotes, filhos de Aarão, 


derramarão o seu sangue em redor do altar. 12 A vítima será, em seguida, 
cortada em pedaços, com a cabeça e a gordura, que o sacerdote disporá 
sobre a lenha colocada no fogo do altar. 13 As entranhas e as pernas serão 
lavadas com água, e, em seguida, o sacerdote oferecerá tudo isso, 
queimando-o no altar. Esse é um holocausto, um sacrifício consumido pelo 
fogo, de odor agradável ao Senhor. 

14 Se a sua oferta ao Senhor for um holocausto tirado dentre as aves, 
oferecerá rolas ou pombinhos. 15 O sacerdote porá a ave sobre o altar, lhe 
destroncará a cabeça e a queimará no altar, depois de haver espremido o seu 
sangue contra a parede do altar. 16 Tirará o papo com as penas e os jogará 
perto do altar, para o oriente, no lugar onde se põem as cinzas. 17 Abrirá em 
seguida a ave à altura das asas, sem as desprender, e a queimará no altar, em 
cima da lenha que está no fogo. Esse é um holocausto, um sacrifício 
consumido pelo fogo, de odor agradável ao Senhor”. 


"""
salvar_para_csv(texto_puro, "Lv", 1, "biblia_levitico1.csv")
