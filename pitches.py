from crypt import methods
from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app =Flask(__name__)

app.config['SECRET_KEY']='190b6b2c1c409cce5aa9432a723f1f45'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)