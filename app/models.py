from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True, index=True)
    categoria = db.Column(db.String(50), nullable=False)
    unidade_medida = db.Column(db.String(10), nullable=False, default='kg')
    dias_validade_padrao = db.Column(db.Integer, nullable=False, default=7)
    
    # Relacionamento com movimentações
    movimentacoes = db.relationship('MovimentacaoEstoque', backref='produto', lazy=True)

    def __repr__(self):
        return f'<Produto {self.nome}>'


class MovimentacaoEstoque(db.Model):
    __tablename__ = 'movimentacoes_estoque'

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False, index=True)
    quantidade = db.Column(db.Float, nullable=False)
    tipo_movimentacao = db.Column(db.String(10), nullable=False) # 'ENTRADA' ou 'SAIDA'
    produtor_origem = db.Column(db.String(120), nullable=True)
    data_colheita = db.Column(db.Date, nullable=False)
    data_validade = db.Column(db.Date, nullable=False, index=True)
    data_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Movimentacao {self.tipo_movimentacao} - {self.quantidade}kg de Produto ID {self.produto_id}>'