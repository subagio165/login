from flask import Flask, render_template, url_for, redirect, flash, redirect, session, request
from app import app, db, s
from app.models import User, Post
from app.forms import RegistrasiForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required
import base64


@app.route('/')
def home():
	user = User.query.all()
	posts = Post.query.all()
	return render_template('home.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated :
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and form.password.data :
			login_user(user)
			return redirect(url_for('home'))
		else :
			flash('Login gagal', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated :
		return redirect(url_for('home')) 
	form = RegistrasiForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, password=form.password.data, email=form.email.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Registrasi {form.username.data} Berhasi', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Reg', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home')) 


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(judul = form.judul.data, isi=form.isi.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash(f'{form.judul.data} Berhasil di upload', 'success')
		return redirect(url_for('home'))
	return render_template('isi_konten.html', title='isi konten', form=form)

@app.route("/post/<post_id>")
def post(post_id):
	post_id = s.loads(post_id)
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title=post.judul, post=post)


@app.route('/upload_gambar', methods=['GET', 'POST'])
@login_required
def upload_gambar():
	if request.method == 'POST':
		gambar = request.files['gambar']
		gambar_string = base64.b64encode(gambar.read())
		hasil = request.args.get(gambar_string)
		return '<h1> hasilnya adalah : {}</h1>' .format(gambar_string)
	return render_template('gambar.html')