from flask import Flask, render_template
from users import Users
from flask_bootstrap import Bootstrap5

EMAIL = "admin@email.com"

PASSWORD = "12345678"

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "Decani"
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['Get', 'POST'])
def login():
    form = Users()
    if form.validate_on_submit():
        if form.email.data == EMAIL and form.password.data == PASSWORD:
            return render_template("./success.html")
        else:
            return render_template("./denied.html")
    else:
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
