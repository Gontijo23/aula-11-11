from flask import Flask
from flask_restful import reqparse, Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =
'postgresql://postgres:adm@localhost/postgres?options=-csearch_path=empresa'
db = SQLAlchemy(app)
marshmallow = Marshmallow(app)



#---------------------1--------------------#

class ProdutoDataBase(db.Model):
        __tablename__ = "Produto"
        id = db.Column(db.Integer, primary_key = True)
        nome = db.Column(db.String(256), unique = True, nullable = False)
        quantidade = db.Column(db.Numeric(precision = 10,), nullable = False)
        preco = db.Column(db.Numeric(precision = 10, scale = 2), nullable = False)
    def __init__(self, nome, preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __repr__(self):
    return f"{self.id, self.nome, self.preco, self.quantidade}"
class ProdutoDataBaseSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
    model = ProdutoDataBase
    sqla_session = db.session
    id = fields.Number()#dump_only=True)
    nome = fields.String(required=True)
    quantidade = fields.Number(required=True)
    preco = fields.Float(required=True)
    api = Api(app)
    # Parse dos dados enviados na requisição no formato JSON:
    parser = reqparse.RequestParser()
    parser.add_argument('codigo', type=int, help='identificador do produto')
    parser.add_argument('nome', type=str, help='nome do produto')
    parser.add_argument('quantidade', type=int, help='quantidade do produto')
    parser.add_argument('preco', type=float, help='preço do produto')


# Produto:
# 1) Apresenta um único produto.
# 2) Remove um único produto.
# 3) Atualiza (substitui) um produto.
class Produto(Resource):
    def get(self, id):
        produto = ProdutoDataBase.query.get(id)
        produto_schema = ProdutoDataBaseSchema()
        resp = produto_schema.dump(produto)
        return {"produto": resp}, 200 #200: Ok
    def delete(self, id):
        produto = ProdutoDataBase.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        return '', 204 #204: No Content
    def put(self, id):
            produto_json = parser.parse_args()
            produto = ProdutoDataBase.query.get(id)
        if produto_json.get('nome'):
            produto.nome = produto_json.nome
        if produto_json.get('preco'):
            produto.preco = produto_json.preco
        if produto_json.get('quantidade'):
            produto.quantidade = produto_json.quantidade
        db.session.add(produto)
        db.session.commit()
        produto_schema = ProdutoDataBaseSchema(only=['id', 'nome', 'preco', 'quantidade'])
        resp = produto_schema.dump(produto)
        return {"produto": resp}, 200 #200: OK
# ListaProduto:
# 1) Apresenta a lista de produtos.
# 2) Insere um novo produto.
class ListaProduto(Resource):
    def get(self):
        produtos = ProdutoDataBase.query.all()
        produto_schema = ProdutoDataBaseSchema(many=True) # Converter objto Python
        para JSON.
        resp = produto_schema.dump(produtos)
        return {"produtos": resp}, 200 #200: Ok
def post(self):
    produto_json = parser.parse_args()
    produto_schema = ProdutoDataBaseSchema()
    produto = produto_schema.load(produto_json)
    produtoDataBase = ProdutoDataBase(produto['nome'], produto['quantidade'], produto['preco'])
    resp = produto_schema.dump(produtoDataBase.create())
    return {"produto": resp}, 201 #201: Created
## Roteamento de recursos:
##
api.add_resource(Produto, '/produtos/<id>')
api.add_resource(ListaProduto, '/produtos')
if __name__ == '__main__':
with app.app_context():
db.create_all()
app.run(debug=True)






#-----------------2--------------------#

class PagamentoDataBase(db.Model):
        __tablename__ = "Folha_Pagamento"
        cpf = db.Column(db.Integer, primary_key = True)
        nome = db.Column(db.String(256), unique = True, nullable = False)
        horas_trabalhadas = db.Column(db.Numeric(precision = 10,), nullable = False)
        valor_da_hora = db.Column(db.Numeric(precision = 10, scale = 2), nullable = False)
    def __init__(self, nome, preco,quantidade):
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_da_hora = valor_da_hora
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __repr__(self):
    return f"{self.id, self.nome, self.horas_trabalhadas, self.valor_da_hora}"
class PagamentoDataBaseSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
    model = ProdutoDataBase
    sqla_session = db.session
    cpf = fields.Number()#dump_only=True)
    nome = fields.String(required=True)
    horas_trabalhadas = fields.Number(required=True)
    valor_da_hora = fields.Float(required=True)
    api = Api(app)
    # Parse dos dados enviados na requisição no formato JSON:
    parser = reqparse.RequestParser()
    parser.add_argument('cpf', type=int, help='identificador do produto')
    parser.add_argument('nome', type=str, help='nome do produto')
    parser.add_argument('horas_trabalhadas', type=int, help='quantidade do produto')
    parser.add_argument('valor_da_hora', type=float, help='preço do produto')
class Folha(Resource):
    def get(self, cpf):
        pagamento = PagamentoDataBase.query.get(cpf)
        pagamento_schema = PagamentoDataBaseSchema()
        resp = pagamento_schema.dump(Folha)
        return {"pagamento": resp}, 200 #200: Ok
    def delete(self, cpf):
        pagamento = PagamentoDataBase.query.get(cpf)
        db.session.delete(pagamento)
        db.session.commit()
        return '', 204 #204: No Content
    def put(self, cpf):
            pagamento_json = parser.parse_args()
            pagamento = PagamentoDataBase.query.get(cpf)
        if pagamento_json.get('nome'):
            pagamento.nome = pagamento_json.nome
        if pagamento_json.get('horas trabalhadas'):
            pagamento.preco = pagamento_json.horas_trabalhadas
        if pagamento_json.get('valor da hora'):
            pagamento.quantidade = pagamento_json.valor_da_hora
        db.session.add(pagamento)
        db.session.commit()
        produto_schema = ProdutoDataBaseSchema(only=['id', 'nome', 'horas trabalhadas', 'valor da hora'])
        resp = produto_schema.dump(pagamento)
        return {"pagamento": resp}, 200 #200: OK
class FolhaPagamento(Resource):
    def get(self):
        pagamento = PagamentoDataBase.query.all()
        pagamento_schema = PagamentoDataBaseSchema(many=True) # Converter objto Python
        para JSON.
        resp = pagamento_schema.dump(pagamento)
        return {"pagamentos": resp}, 200 #200: Ok
def post(self):
    pagamento_json = parser.parse_args()
    pagamento_schema = PagamentoDataBaseSchema()
    pagamento = pagamento_schema.load(pagamento_json)
    pagamentoDataBase = PagamentoDataBase(pagamento['nome'], pagamento['horas trabalhadas'], pagamento['valor da hora'])
    resp = pagamento_schema.dump(pagamentoDataBase.create())
    return {"pagamento": resp}, 201 #201: Created
## Roteamento de recursos:
##
api.add_resource(pagamento, '/pagamento/<cpf>')
api.add_resource(FolhaPagamento, '/pagamento')
if __name__ == '__main__':
with app.app_context():
db.create_all()
app.run(debug=True)
