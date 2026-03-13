from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

class RegisterForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Register')

@app.route('/', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return render_template("success.html")

    return render_template("register.html", form=form)

app.run(debug=True)
