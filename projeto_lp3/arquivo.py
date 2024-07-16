#ler o arquivo 
# open -> abri o arquivo -> carrega os dados do arquivo em memória 
arquivo = open("projeto_lp3/dados.txt") #nome do arquivo -> é o caminho do arquivo -> tem que colocar o caminho completo 
#retorna TEXTAOWROPPER -> representa os dados do arquivo em memória 

#read -> ler o todo o conteudo do arquivo que está em memoria 
#chamar o read multiplas vezes -> não vai funcionar -> pegou uma vez, não pode ler dnv 
conteudo = arquivo.read()
print(conteudo.lower())
arquivo.close()

#with -> abre algum tipo de estrutura e vai fechar automaticamenbte quando o código sair do escopo do bloco -> tipo no if
with open("projeto_lp3/dados.txt") as arquivo2:
    #o arquivo será fechado quando a execução sair do escopo do bloco 
    conteudo2 = arquivo2.read() 
    print(conteudo2)

with open("projeto_lp3/dados.txt") as arquivo3:
    conteudo3 = arquivo3.readlines() 
    #readlines() -> devolve uma lista de String 
    print(conteudo3)

with open("projeto_lp3/dados.txt", "r") as arquivo4: 
    #existe um parametro para passar o modo como vai ler -> mode = 'r' -> é padrão
    linhas = []
    for linha in arquivo4: 
        #considera o arquivo uma lista de linhas 
        linhas.append(linha.strip())
    print(linhas)

# with open("projeto_lp3/dados.txt", "w") as arquivo5:
#     #abrir no modo escrita 
#     # arquivo5.write("JACA") #SUBSTITUI
#     pass #pq nao pode ter bloco sem código -> o arquivo não fecha com o pass 

with open("projeto_lp3/dados.txt", "a") as arquivo6:
    #abrir com a letra a -> append
    arquivo6.write("\nmaçã")

def obter_produtos():
    with open("projeto_lp3/produto.csv", "r") as produto_arquivo:
        produtos = []
        for linha in produto_arquivo:
            dados_produto = linha.strip().split(",")
            produto ={
                "nome": dados_produto[0],
                "descricao": dados_produto[1],
                "preco": float(dados_produto[2]),
                "imagem": dados_produto[3]
            }
            produtos.append(produto)
        return produtos

def salvar_produto(nome, descricao, preco, img):
    with open("projeto_lp3/produto.csv", "a") as arquivo_produto: 
        produto =  f"{nome},{descricao},{preco},{img}"
        arquivo_produto.write(f"\n{produto}")

# salvar_produto('suco de uva', 'é bom', '10', 'lala.png')