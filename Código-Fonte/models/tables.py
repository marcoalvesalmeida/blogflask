from blog import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class Usuario(db.Model):
	__tablename__ = "usuarios";

	id = db.Column(db.Integer, primary_key=True)
	nome_de_usuario = db.Column(db.String(50), unique=True)
	senha = db.Column(db.String)
	nome = db.Column(db.String)
	email = db.Column(db.String, unique=True)

	def __init__(self, nome_de_usuario, senha, nome, email):
		self.nome_de_usuario = nome_de_usuario
		self.senha = senha
		self.nome = nome
		self.email = email

	def __repr__(self):
		return "<Usuario %r>" % self.nome_de_usuario

	#Parte Responsável pelo Login abaixo
	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)


class Post(db.Model):
	__tablename__ = "posts"

	id = db.Column(db.Integer, primary_key=True)
	conteudo = db.Column(db.Text)
	id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

	usuario = db.relationship('Usuario', foreign_keys=id_usuario)

	def __init__(self, conteudo, id_usuario):
		self.conteudo = contudo
		self.id_usuario = id_usuario

	def __repr__(self):
		return "<Post %r>" % self.id

class Segue(db.Model):
	__tablename__ = "segue"
	id = db.Column(db.Integer, primary_key=True)
	id_usuario = db.Column(db.Integer, ForeignKey('usuarios.id'))
	id_seguidor = db.Column(db.Integer, ForeignKey('usuarios.id'))

	usuario = db.relationship('Usuario', foreign_keys=id_usuario)
	seguidor = db.relationship('Usuario', foreign_keys=id_seguidor)
