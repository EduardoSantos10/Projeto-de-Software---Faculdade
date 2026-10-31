from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Produto, MovimentacaoEstoque

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Redireciona para a Tela 1 (Login / Entrada Principal)
    return redirect(url_for('main.login'))

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Tela 1: Entrada principal ou menu inicial (Autenticação)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Validação simples de MVP para a coordenadora Dona Helena
        if username == 'helena.coordenadora@ecobairro.org' and password == 'ecobairro2026':
            return redirect(url_for('main.dashboard'))
        else:
            flash('Credenciais inválidas. Verifique o e-mail e a senha.', 'danger')
    return render_template('login.html')

@main_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Tela 2: Execução da funcionalidade central (Registo de Entradas - RF01)
    produtos = Produto.query.all()
    
    if request.method == 'POST':
        try:
            produto_id = int(request.form.get('produto_id'))
            quantidade = float(request.form.get('quantidade'))
            produtor = request.form.get('produtor_origem')
            colheita_str = request.form.get('data_colheita')
            
            data_colheita = datetime.strptime(colheita_str, '%Y-%m-%d').date()
            produto = Produto.query.get(produto_id)
            
            # Cálculo automático do shelf-life (data de validade)
            from datetime import timedelta
            data_validade = data_colheita + timedelta(days=produto.dias_validade_padrao)
            
            nova_mov = MovimentacaoEstoque(
                produto_id=produto_id,
                quantidade=quantidade,
                tipo_movimentacao='ENTRADA',
                produtor_origem=produtor,
                data_colheita=data_colheita,
                data_validade=data_validade
            )
            
            db.session.add(nova_mov)
            db.session.commit()
            flash('Safra registada com sucesso!', 'success')
            return redirect(url_for('main.relatorio'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao registar entrada: {str(e)}', 'danger')
            
    return render_template('entrada.html', produtos=produtos)

@main_bp.route('/relatorio')
def relatorio():
    # Tela 3: Alertas, listagem e resultados (RF02 / RF03)
    movimentacoes = MovimentacaoEstoque.query.order_by(MovimentacaoEstoque.data_validade.asc()).all()
    hoje = datetime.now().date()
    
    return render_template('inventario.html', movimentacoes=movimentacoes, hoje=hoje)