from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from app import db, bcrypt
from flask import session
import re


auth_bp = Blueprint('auth', __name__)

def validate_password(password):
    if len(password) < 6:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[\W_]", password):  # caractere especial
        return False
    return True


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Verifica se já existe usuário ou email no banco
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash("Usuário ou email já cadastrado.", "error")
            return redirect(url_for('auth.register'))

        # Validação da senha
        if not validate_password(password):
            flash("Senha inválida. Mínimo 6 caracteres, incluindo letra, número e caractere especial.", "error")
            return redirect(url_for('auth.register'))

        # Criação do novo usuário
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("Cadastro realizado com sucesso! <a href='/login'>Ir para login</a>", "success")
        return redirect(url_for('auth.register'))

    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            flash(f"Bem-vindo, {user.username}!", "success")
            return redirect(url_for('index'))  # vai para a página inicial
        else:
            flash("Credenciais inválidas", "error")
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Você saiu da conta.", "info")
    return redirect(url_for('auth.login'))
