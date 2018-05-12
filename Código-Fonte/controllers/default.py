from flask import render_template, flash, url_for, redirect, jsonify, request
from blog import blog, db, lm
from blog.models.forms import LoginForm
from flask_login import login_user, logout_user
from blog.models.tables import Usuario

@lm.user_loader
def load_user(id):
    return Usuario.query.filter_by(id=id).first()

@blog.route("/<usuario>")
@blog.route("/", defaults={"usuario": None})
def index(usuario):
	return render_template('index.html',usuario=usuario)

@blog.route("/base")
def base():
	return render_template('base.html')

@blog.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		usuario = Usuario.query.filter_by(email=form.email.data).first()
		if usuario and usuario.senha == form.senha.data:
			login_user(usuario)
			return render_template('index.html',usuario=usuario)
		else:
			flash("Email ou senha incorretos!")
	return render_template('login.html', form=form)

@blog.route("/inserir")
def inserir():
	usuario = Usuario('marcoalves','1234','Marco Alves de Almeida','marcoalvesneto@gmail.com')
	db.session.add(usuario)
	db.session.commit()
	return "ok"

@blog.route("/listar")
def listar():
	usuario = None
	usuario = Usuario.query.filter_by(email="marcoalvesneto@gmail.com").first()
	if usuario:
		print(usuario.nome)
	return render_template('index.html',usuario=usuario)

@blog.route("/atualizar")
def atualizar():
	usuario = Usuario.query.filter_by(email="marcoalvesneto@gmail.com").first()
	usuario.nome_de_usuario = "marco.a.a"
	db.session.add(usuario)
	db.session.commit()
	return "Ok"

@blog.route("/deletar")
def deletar():
	usuario = Usuario.query.filter_by(id=1).first()
	db.session.delete(usuario)
	db.session.commit()
	return "OK"

@blog.route("/logout")
def logout():
	logout_user()
	flash("Você saiu do sistema!")
	return redirect(url_for("login"))

@blog.route('/verifica_email', methods=['GET','POST'])
def verifica_email():
    valido = 0
    email = request.args.get('email', None, type=None)
    senha = request.args.get('senha', None, type=None)
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and senha==usuario.senha:
        valido = 1
        return render_template('index.html',usuario=usuario)
    return jsonify(result=valido)
