
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm


app =Flask(__name__)
app.config['SECRET_KEY']='190b6b2c1c409cce5aa9432a723f1f45'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.model):
    id = db.column(db.Integer,primary_key=True)
    username =db.Column(db.String(15),unique=True,nullable=False)
    username = db.Column(db.String(100),unique=True,nullable=False)
    image_file = db.Collumn(db.String(28),nullable=False,default='default.jpg')
    password = db.Column(db.String(35),nullable=False)
    

posts = [
    {
        'author':'Karen Johns',
        'title':'Pitches Post 1',
        'content':'First Post Content',
        'date_posted':'January 26,2022'
        
    },
    {
        'author':'Teddy Lorrens',
        'title':'Pitches Post 2',
        'content':'Second Post Content',
        'date_posted':'January 30,2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Your account {form.username.data} created!','successs')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'george@pitches.com' and form.password.data == '12345':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful.please check email and password','danger')
    return render_template('login.html', title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)