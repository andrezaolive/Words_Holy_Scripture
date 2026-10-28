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
texto_puro = """1 Subiu Moisés das planícies de Moab ao monte Nebo, ao cimo do 
Fasga, defronte de Jericó. O Senhor mostrou-lhe toda a terra, desde 
Galaad até Dà, 2 todo o Neftali, a terra de Efraim e de Manassés, todo o 
território de Judá até o mar ocidental, 3 o Negueb, a planície do Jordão, o 
vale de Jericó, a cidade das palmeiras, até Segor. 4 O Senhor disse-lhe: “Eis 
a terra que jurei a Abraão, a Isaac e a Jacó dar à sua posteridade. Viste-a 
com os teus olhos, mas não entrarás nela”. 
5 E Moisés, o servo do Senhor, morreu ali na terra de Moab, como o Senhor 
decidira.” 6 E ele o enterrou no vale da terra de Moab, defronte de Bet- 
Fegor, e ninguém jamais soube o lugar do seu sepulcro. 7 Moisés tinha 
cento e vinte anos no momento de sua morte: sua vista não se tinha 
enfraquecido, e o seu vigor não se tinha abalado. 8 Os israelitas choraram- 
no durante trinta dias, nas planícies de Moab, e, passado esse tempo, 
acabaram-se os dias de pranto consagrados ao luto por Moisés. 9 Josué, 
filho de Nun, ficou cheio do espírito de sabedoria, porque Moisés lhe tinha 
imposto as suas mãos. Os israelitas obedeceram-lhe, assim como o Senhor 
tinha ordenado a Moisés. 

10 Não se levantou mais em Israel profeta comparável a Moisés, com 
quem o Senhor conversava face a face. 11 (Ninguém o igualou) quanto a 
todos os sinais e prodígios que o Senhor o mandou fazer na terra do Egito, 
diante do faraó, de seus servos e de sua terra, 12 nem quanto a todos os 
feitos e às terríveis ações que ele operou sob os olhos de todo o Israel. 

"""
salvar_para_csv(texto_puro, "Dt", 34, "biblia_deuteronomio34.csv")
