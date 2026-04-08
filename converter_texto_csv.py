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
texto_puro = """1 O Senhor disse a Moisés: “Dize aos israelitas o seguinte: 2 Se alguém 
fizer um voto com respeito às pessoas, essas serão do Senhor, segundo 
a tua avaliação. 3 Se se tratar de um homem de vinte a sessenta anos, o valor 
será de cinquenta siclos de prata, conforme o siclo do santuário, 4 se for 
uma mulher, o valor será de trinta siclos. 5 Para a idade de cinco a vinte 
anos, o valor será de vinte siclos para o menino, e dez siclos para a menina. 
6 De um mês até cinco anos, o valor será de cinco siclos de prata para um 
menino, e três para uma menina. 7 Aos sessenta anos, e daí para cima, a 
estimação será de quinze siclos para um homem e dez siclos para uma 
mulher. 8 Se aquele que tiver feito o voto for demasiado pobre e não puder 
pagar o valor que avaliaste, será apresentado ao sacerdote, que fixará o 
valor segundo as posses daquele que fez o voto. 
9 Se se tratar de animais que se podem oferecer ao Senhor, todo animal que 
assim se tiver dado ao Senhor será coisa santa. 10 Não poderá ser trocado 
nem substituído, bom por mau, ou mau por bom. Mas, se se trocar um 
animal por outro, eles serão coisa santa, tanto um como o outro. 11 Se se 
tratar de um animal impuro que não se pode oferecer ao Senhor, será 
apresentado ao sacerdote: 12 ele o avaliará, conforme for bom ou mau, e sua 
estimação determinará o preço. 13 Se se quiser resgatá-lo, ajuntará uma 
quinta parte ao que tiver sido avaliado. 

14 Se alguém consagrar ao Senhor a sua casa fazendo dela coisa santa, o 
sacerdote a avaliará segundo for boa ou má, e ela será vendida pelo preço 
dessa avaliação. 15 Mas, se aquele que consagrou a sua casa quiser resgatá- 
la, ajuntará um quinto ao preço da avaliação, e ela lhe pertencerá de novo. 

16 Se alguém consagrar ao Senhor uma parte da terra que lhe pertence, tu 
a avalia-rás segundo a quantidade de grãos que se pode semear nela, à razão 
de cinquenta siclos de prata por homer de cevada. 17 Se consagrar o seu 
campo, a partir do ano do jubileu, se fará segundo a tua avaliação: 18 mas, 
se o tiver feito depois do jubileu, o sacerdote estimará o seu preço segundo 
o número de anos que restam até o jubileu, e haverá uma redução sobre o 
preço da avaliação. 19 Se aquele que consagrou o seu campo quiser resgatá- 
lo, ajuntará um quinto ao preço fixado, e o campo lhe pertencerá. 20 Se não 
o resgatar e o vender a outro, esse campo não poderá mais ser resgatado. 21 
Quando o campo ficar livre no jubileu, será consagrado ao Senhor como um 
campo votado ao interdito, e passará a ser propriedade do sacerdote. 

22 Se alguém consagrar ao Senhor um campo que comprou, o qual não 
faça parte de seu patrimônio, 23 o sacerdote fixará o seu preço de acordo 
com a tua avaliação até o ano do jubileu, e esse homem pagará o preço 
fixado no mesmo dia, é uma coisa consagrada ao Senhor. 24 No ano jubilar, 
o campo voltará ao vendedor, como patrimônio que lhe pertence. 25 Todas 
as avaliações se farão em siclos do santuário. O siclo vale vinte gueras. 

26 Entretanto, ninguém poderá consagrar os primogênitos de seu gado, 
pois pertencem já ao Senhor pelo seu título de primogênito: seja um boi, 
seja uma ovelha, são propriedades do Senhor. 27 Se se tratar de um animal 
impuro, será resgatado pelo preço que fixares, ajuntando-se mais uma 
quinta parte, se não for resgatado, será vendido pelo preço da avaliação. 

28 Se um homem consagrar ao Senhor por interdito alguma coisa que lhe 
pertence, seja qual for esse objeto — uma pessoa, um animal ou um campo 
de seu patrimônio — ela não poderá ser vendida, nem resgatada: tudo o que é 
votado por interdito é coisa consagrada ao Senhor.* 29 Nenhuma pessoa 
votada ao interdito poderá ser resgatada: ela será morta. 

30 Todos os dízimos da terra, tomados das sementes do solo ou dos frutos 
das árvores são propriedades do Senhor: é uma coisa consagrada ao Senhor. 
31 Se alguém quiser resgatar alguma coisa de seus dízimos, ajuntará uma 
quinta parte. 32 Todos os dízimos do gado maior e menor, os dízimos do que 
passa sob o cajado do pastor, o décimo (animal) serão consagrados ao 
Senhor. 33 Não se fará escolha entre bom e mau e não se fará substituição. 
Se alguém o fizer, tanto o animal substituído como o que substituiu serão 
coisa consagrada: não poderão ser resgatados”. 

34 Tais são as ordenações que o Senhor deu a Moisés para os israelitas, no 
monte Sinai. 
"""
salvar_para_csv(texto_puro, "Lv", 27, "biblia_levitico27.csv")
