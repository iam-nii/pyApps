# Importing the necessary libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, FLOAT


# # Create the database if it doesn't exist
# db = sqlite3.connect("books-collection.db")
#
# # Create a database cursor for adding, editing and deleting rows of data
# cursor = db.cursor()
#
# # Creating a table
# cursor.execute("CREATE TABLE IF NOT EXISTS books("
#                "id integer PRIMARY KEY, "
#                "title varchar(25  0) NOT NULL UNIQUE,"
#                "author varchar(250) NOT NULL, "
#                "rating float NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Rich Dad Poor Dad', 'Robert Kiyosaki', '8.3')")
# db.commit()

# Initializing the extension

# Creating the database

app = Flask(__name__)

class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)

db.init_app(app)

# Creating a new table

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(FLOAT, nullable=True, default=0)


with app.app_context():
    db.create_all()

# ---------------- CRUD operations -------------------- #

# Creating a new record
# with app.app_context():
#     # The primary key can be omitted in this case. It will be auto-generated
#     new_book = Books(title="The 7 habits of effective people", author="Nii", rating="9.8")
#     db.session.add(new_book)
#     db.session.commit()

# Reading records from the db
with app.app_context():
    # The query
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

#     Reading a particular record from the table
with app.app_context():
    result = db.session.execute(db.select(Books).where(Books.id == 1))
    print(result.scalar().title)


# Updating data in the database
with app.app_context():
    update = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
    update.title = "Rich Dad poor dad"
    db.session.commit()

#    Updating a record by PRIMARY KEY
with app.app_context():
    update = db.get_or_404(Books, 2)
    update.title = "The Merry Men"
    db.session.commit()


