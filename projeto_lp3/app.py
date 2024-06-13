#vamos usar do Flask 
from flask import Flask
#importando a classe Flask do módulo flask 
from validate_docbr import CPF, CNPJ


# Aluno a1 = new Aluno();
# a1 = Aluno() -> equivalente 

app = Flask("Minha Aplicação")
cpf = CPF()
cnpj = CNPJ()
#"Minha aplicação" -> nome (atributo) do objeto 
#instancia um objeto flask que representa a aplicação

#rota + função 
#rota: definição de um padrão url 
#função: função python com retorno (string, template, outro)

#página home - / (padrão da home é o barra)
@app.route("/")
#toda vez que marcar / acessa a página home 
def home(): 
    return "<h1>Home page</h1>"
#página contato - /contato 
@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"
#página produtos - /produtos 
@app.route("/produtos")
def produtos():
    return "<h1>Lista de produtos</h1>"
#o que aparece na url -> é a rota 

# /gerar_cpf (deve devolver um cpf aleatório)
# /servicos (deve devolver um título "Nossos servicos")
# /gerar_cnpj (deve devolver um cnpj aleatorio)

@app.route("/gerar_cpf")
def gerar_cpf():
    cpf_usuario = cpf.generate(True)
    return f"<h1>Gerar CPF</h1><p>CPF: {cpf_usuario}"

@app.route("/servicos")
def servicos():
    return "<h1>Nossos servicos</h1>"
#o que aparece na url -> é a rota 

@app.route("/gerar_cnpj")
def gerar_cnpj():
    cnpj_usuario = cnpj.generate(True)
    return "<div> O seu cnpj é "+ cnpj_usuario + "<div>"