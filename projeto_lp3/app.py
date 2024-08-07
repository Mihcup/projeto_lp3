#vamos usar do Flask 
from flask import Flask, render_template, request
#importando a classe Flask do módulo flask 
from validate_docbr import CPF, CNPJ


# Aluno a1 = new Aluno();
# a1 = Aluno() -> equivalente 

app = Flask("Minha Aplicação")
cpf = CPF()
cnpj = CNPJ()
#"Minha aplicação" -> nome (atributo) do objeto 
#instancia um objeto flask que representa a aplicação

#página home - / (padrão da home é o barra)
@app.route("/")
#toda vez que marcar / acessa a página home 
def home(): 
    return render_template("home.html")

#página contato - /contato 
@app.route("/contato")
def contato():
    return render_template("contatos.html")

#página produtos - /produtos 
lista_produtos=[
        {"nome": "Coca-cola", "descricao":"Mata a sede"}, 
        {"nome": "doritos", "descricao":"suja a mão"},
        {"nome":"Chocolate", "descricao":"bom"}
        #a lista poderia vir do bdd 
    ]
@app.route("/produtos")
def produtos():
    return render_template("produtos.html",produtos=lista_produtos)

#o que aparece na url -> é a rota 
# /gerar_cpf (deve devolver um cpf aleatório)
# /servicos (deve devolver um título "Nossos servicos")
# /gerar_cnpj (deve devolver um cnpj aleatorio)

#exercício 1 e 2
@app.route("/gerar_cpf")
def gerar_cpf():
    cpf_usuario = cpf.generate(True)
    return render_template("cpf.html",cpf=cpf_usuario)


@app.route("/gerar_cnpj")
def gerar_cnpj():
    cnpj_usuario = cnpj.generate(True)
    return render_template("cnpj.html",cnpj=cnpj_usuario)


#aula 25/06
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods=['POST'])
def salvar_produtos():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {'nome': nome, "descricao": descricao}
    lista_produtos.append(produto) 
    return render_template("produtos.html", produtos=lista_produtos)
    # a lista tem que ficar global

app.run()



#códigos das últimas aulas: 

#---------------------------------------------
# #página contato - /contato 
# @app.route("/contato")
# def contato():
#     return "<h1>Contato</h1>"

#-----------------------------------------------
# #página produtos - /produtos 
# @app.route("/produtos")
# def produtos():
#     return "<h1>Lista de produtos</h1>"

#---------------------------------------------
#rota + função 
#rota: definição de um padrão url 
#função: função python com retorno (string, template, outro)