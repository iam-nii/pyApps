from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, FLOAT

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

all_books = []

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookshelf.db"

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(FLOAT, nullable=True, default=0)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        data = db.session.execute(db.select(Books).order_by(Books.title)).scalars()
        for book in data:
            all_books.append({
                'Title': book.title,
                'Author': book.author,
                'Rating': book.rating,
            })

    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    global all_books
    if request.method == "GET":
        return render_template("add.html")

    if request.method == 'POST':
        book_name = request.form['bookName']
        book_author = request.form['bookAuthor']
        book_rating = request.form['bookRating']
        all_books.append(
            {
                'Title': book_name,
                'Author': book_author,
                'Rating': book_rating,
            }
        )
        # Saving the data to a database
        with app.app_context():
            new_book = Books(title=request.form['bookName'], author=request.form['bookAuthor'],
                             rating=request.form['bookRating'])
            db.session.add(new_book)
            db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

