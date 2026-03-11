import re
import csv

def salvar_para_csv(texto_bruto, sigla_livro, capitulo, nome_arquivo):
    # Limpa espaços e quebras de linha duplas
    texto_unificado = re.sub(r'\s+', ' ', texto_bruto).strip()

    # Regex que identifica: [Número] [Espaço] [Letra Maiúscula]
    # Isso evita capturar números como "2 de cada espécie" no meio da frase como versiculo
    padrao = r'(\d+)\s+([A-Z].+?)(?=\s+\d+\s+[A-Z]|$)'
    
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
texto_puro = """1 O Senhor disse a Noé: “Entra na arca, tu e toda a tua casa, porque te 
reconheci justo diante dos meus olhos, entre os de tua geração. 2 De 
todos os animais puros tomarás sete casais, machos e fêmeas, e de todos os 
animais impuros tomarás um casal, macho e fêmea; 3 das aves do céu 
igualmente sete casais, machos e fêmeas, para que se conserve viva a raça 
sobre a face de toda a terra. 4 Dentro de sete dias farei chover sobre a terra 
durante quarenta dias e quarenta noites, e exterminarei da superfície da terra 
todos os seres que eu fiz”. 5 Noé fez tudo o que o Senhor lhe tinha 
ordenado. 
6 Noé tinha seiscentos anos quando veio o dilúvio sobre a terra. 7 Para 
escapar à inundação, entrou na arca com seus filhos, sua mulher e as 
mulheres de seus filhos. 8 Dos animais puros e impuros, das aves e de tudo 

que se arrasta sobre a terra, 9 entraram na arca com Noé um casal macho e 
fêmea, como o Senhor tinha ordenado a Noé. 10 Passados os sete dias, as 
águas do dilúvio precipitaram-se sobre a terra. 

11 No ano seiscentos da vida de Noé, no segundo mês, no décimo sétimo 
dia do mês, romperam-se naquele dia todas as fontes do grande abismo, e 
abriram-se as barreiras do céu. 12 A chuva caiu sobre a terra durante 
quarenta dias e quarenta noites. 13 Naquele mesmo dia, entrou Noé na arca, 
com Sem, Cam e Jafé, seus filhos, sua mulher e as três mulheres de seus 
filhos; 14 e com eles os animais selvagens de toda a espécie, os animais 
domésticos de toda a espécie, os répteis de toda a espécie que se arrastavam 
sobre a terra, e tudo o que voa, de toda a espécie, todas as aves e tudo o que 
tem asas. 15 De cada espécie que tem um sopro de vida um casal entrou na 
arca com Noé. 16 Eles chegavam, macho e fêmea, de cada espécie. Como 
Deus tinha ordenado a Noé. E o Senhor fechou a porta atrás dele. 

17 O dilúvio caiu sobre a terra durante quarenta dias. As águas incharam e 
levantaram a arca, que foi elevada acima da terra. 18 As águas inundaram 
tudo com violência, e cobriram toda a terra, e a arca flutuava na superfície 
das águas. 19 As águas engrossaram prodigiosamente sobre a terra, e 
cobriram todos os altos montes que existem debaixo do céu; 20 e elevaram- 
se quinze côvados acima dos montes que cobriam. 21 Todas as criaturas que 
se moviam na terra foram exterminadas: aves, animais domésticos, feras 
selvagens e tudo o que se arrasta na terra, e todos os homens. 22 Tudo o que 
respira e tem um sopro de vida sobre a terra pereceu. 23 Assim foram 
exterminados todos os seres que se encontravam sobre a face da terra, desde 
os homens até os quadrúpedes, tanto os répteis como as aves do céu, tudo 
foi exterminado da terra. Só Noé ficou e o que se encontrava com ele na 
arca. 24 As águas cobriram a terra pelo espaço de cento e cinquenta dias. 
"""
salvar_para_csv(texto_puro, "Gen", 7, "biblia_genesis7.csv")