from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Email
from app.models import User

class RegistrasiForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	submit = SubmitField('Daftar')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username Sudah Ada Silahkan Pilih Yang Lain')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email Sudah Ada Silahkan Pilih Yang Lain')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Masuk')


class PostForm(FlaskForm):
	judul = StringField('Judul', validators=[DataRequired()])
	isi = TextField('Isi', validators=[DataRequired()])
	submit = SubmitField('post')

