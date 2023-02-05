from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor(a)': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'O Vento Levou',
        'autor(a)': 'Margaret Mitchell'
    },
    {
        'id': 3,
        'titulo': 'O Menino da Lua',
        'autor(a)': 'Ziraldo Alves Pinto'
    },
]


# Consultar(Todos)
@app.route('/livros',methods=['GET']) #Rotas
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def atualizar_livros_por_id(id):
    livro_atualizar = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_atualizar)
            return jsonify(livros[indice])
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

app.run(port=5280,host='localhost',debug=True)