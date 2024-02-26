from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('recruto.html', name=name, message=message)


@app.route('/')
def home():
    return 'Добро пожаловать!'


if __name__ == "__main__":
    app.run(debug=True)