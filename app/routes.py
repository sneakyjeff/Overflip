from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, PaymentForm, RegistrationForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/index')
@login_required
def index():
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'I like donuts!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Trump is dump!'
        }
    ]
	return render_template("index.html", title='Home Page', posts=posts)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if '@' in form.username.data:
            user = User.query.filter_by(email=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
        else:
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# @app.route('/edit', methods=['GET', 'POST'])
# def edit():
#     form = AboutForm()
#     if form.validate_on_submit():
#         about_me = form.about.data
#         db.session.add(about_me)
#         db.session.commit()
#         flash('Congratulations, you edited your bio!')
#         return redirect(url_for('index'))
#     return render_template('edit.html', title='Edit', form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@app.route('/make_post', methods=['GET', 'POST'])
@login_required
def make_post():
    return render_template('make_post.html', title='Make Post')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = PaymentForm()
    if form.validate_on_submit():
        flash('Enter name on card {}, remember_me={}'.format(
            form.nameoncard.data, form.remember_me.data))
        return redirect(url_for('index')) #This is where page redirects to after submission
    return render_template('payment.html', title='Payment', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))