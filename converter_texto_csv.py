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
texto_puro = """1 José lançou-se então sobre o rosto de seu pai e o beijou chorando. 2 
 Ordenou depois aos médicos que o serviam que embalsamassem seu 
pai, e os médicos embalsamaram Israel. 3 Gastaram nisso quarenta dias, que 
é o tempo necessário ao embalsamamento. Os egípcios choraram-no 
durante setenta dias. 4 Passado o tempo do pranto, José disse à casa do 
faraó: “Se achei graça aos vossos olhos, dizei de minha parte ao faraó 5 Aque 
meu pai me fez jurar-lhe: ‘Eu vou morrer — disse-me ele —, tu me enterrarás 
no túmulo que adquiri na terra de Canaã’. Permite-me, pois, subir e enterrar 
meu pai, depois voltarei”. 6 O faraó respondeu: “Vai sepultar teu pai como 
ele te fez jurar”. 

7 José partiu para sepultar seu pai. Todos os servos do faraó, os anciãos de 
sua casa e todos os anciãos do Egito, 8 Atoda a casa de José, seus irmãos e a 
casa de seu pai o seguiram. Deixaram na terra de Gessen somente seus 
filhinhos, suas ovelhas e seus bois. 9 Carros e cavaleiros acompanhavam- 
no, de sorte que a caravana era muito grande. 10 Chegando à eira de Atad, 
além do Jordão, fizeram uma grande e solene lamentação, e José celebrou, 
em honra de seu pai, um pranto de sete dias. 11 Vendo esse pranto na eira de 
Atad, o povo daquela terra disse: “Grande pranto é esse dos egípcios!”. Daí 
o nome de Abel-Misraim dado a esse lugar, que está situado além do 
Jordão.* 12 Os filhos de Jacó fizeram, pois, o que ele lhes tinha ordenado. 13 


Levaram-no para Canaã e enterraram-no na caverna da terra de Macpela, 
que Abraão tinha comprado, juntamente com a propriedade de Efron, o 
hiteu, defronte de Mambré, para ter a propriedade de uma sepultura. 

14 Depois do enterro, José voltou para o Egito com seus irmãos e todos os 
que o tinham acompanhado nos funerais de seu pai. 15 Os irmãos de José, 
vendo que seu pai morrera, disseram entre si: “Será que José nos tomará em 
aversão e irá vingar-se de todo o mal que lhe fizemos?”. 16 Mandaram, pois, 
dizer-lhe: “Antes de morrer, teu pai recomendou-nos 17 Aque te pedíssemos 
perdão do crime que teus irmãos cometeram, de seu pecado, de todo o mal 
que te fizeram. Perdoa, pois, agora esse crime àqueles que servem o Deus 
de teu pai”. Ouvindo isso, José chorou. 18 Seus irmãos vieram jogar-se aos 
seus pés, dizendo: “Somos teus escravos!”. 19 José disse-lhes: “Não temais: 
posso eu pôr-me no lugar de Deus? 20 Vossa intenção era de fazer-me mal, 
mas Deus tirou daí um bem, era para fazer, como acontece hoje, com que se 
conservasse a vida a um grande povo. 21 Não temais, pois: eu vos 
sustentarei a vós e a vossos filhos”. Essas palavras, que lhes foram direto ao 
coração, reconfortaram-nos. 

22 José habitou no Egito, e também a família de seu pai. Viveu cento e 
dez anos. 23 Viu os descendentes de Efraim até a terceira geração. 
Igualmente, os filhos de Maquir, filho de Manassés, vieram à luz sobre os 
joelhos de José.* 24 José disse a seus irmãos: “Vou morrer, mas Deus vos 
visitará seguramente e vos fará subir desta terra para a terra que jurou dar a 
Abraão, Isaac e a Jacó”. 25 E José fez que os filhos de Israel jurassem: 
“Quando Deus vos visitar — disse ele — levareis daqui os meus ossos”. 26 
José morreu com a idade de cento e dez anos. Foi embalsamado e 
depositado num sarcófago no Egito. 

"""
salvar_para_csv(texto_puro, "Gen", 50, "biblia_genesis50.csv")
