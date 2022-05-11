from flask import  render_template, url_for, flash, redirect
from pitches import app, db , bcrypt
from pitches.forms import RegistrationForm, LoginForm
from pitches.models import User, Post
from flask_login import login_user



posts = [
    {
        'author': 'Brian Cheruiyot',
        'title': 'Pitches Post 1',
        'content': 'First post content',
        'date_posted': 'May 7, 2022'
    },
    {
        'author': 'Tiffany Haddish',
        'title': 'Pitches Post 2',
        'content': 'Second post content',
        'date_posted': 'May 9, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
         db.session.add(user)
         db.session.commit()
         flash('Your account has been created! You are now able to log in', 'success')
         return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
           flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)