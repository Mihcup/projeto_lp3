#vamos usar do Flask 
from flask import Flask
#importando a classe Flask do módulo flask 

# Aluno a1 = new Aluno();
# a1 = Aluno() -> equivalente 

app = Flask("Minha Aplicação")
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