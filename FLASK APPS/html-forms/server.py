from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        return f"<h1>Name: {request.form['username']}, Password: {request.form['password']}</h1>"
    else:
        return f"<h1>Username: {request.form['username']}, Password: {request.form['password']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)