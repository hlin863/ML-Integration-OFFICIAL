from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form):
    name = TextAreaField('', [validators.DataRequired()])

@app.route('/')

def index():

    form = HelloForm(request.form)

    return render_template('index.html', Form=form)

@app.route('/hello', methods=['POST'])
def hello():

    form = HelloForm(request.form)

    if request.method == 'POST' and form.validate():

        # if the form is valid, redirect to the hello page

        name = request.form['name']

        return render_template('greeting.html', name=name)

    return render_template('index.html', Form=form)

if __name__ == '__main__':

    app.run(debug=True)