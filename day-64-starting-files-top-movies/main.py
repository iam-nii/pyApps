from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Float
from EditForm import EditForm
from AddForm import AddForm

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-10-movies.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[str] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(300), nullable=False)


with app.app_context():
    db.create_all()


# with app.app_context():
#     new_movie = Movies(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film,"
#                     " learn the story of the Sully family (Jake, Neytiri, and their kids), "
#                     "the trouble that follows them, the lengths they go to keep each other safe, "
#                     "the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()
# with app.app_context():
#     movie = db.session.execute(db.select(Movies).where(Movies.id == 3)).scalar()
#     db.session.delete(movie)
#     db.session.commit()

@app.route("/")
def home():
    if request.method == 'GET':
        with app.app_context():
            result = db.session.execute(db.select(Movies))
            all_movies = Movies.query.all()
            print(all_movies)
            # for movie in result:
            #     if movie not in movies:
            #         movies.append({
            #             "id": movie.id,
            #             "title": movie.title,
            #             "year": movie.year,
            #             "description": movie.description,
            #             "rating": movie.rating,
            #             "ranking": movie.ranking,
            #             "review": movie.review,
            #             "url": movie.img_url,
            #         })

    return render_template("index.html", movies=all_movies)


@app.route("/update/<movie_title>", methods=['GET', 'POST'])
def update(movie_title):
    form = EditForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            ranking = form.Rating.data
            review = form.Review.data
            with app.app_context():
                update_movie = db.session.execute(db.select(Movies)
                                                  .where(Movies.title == movie_title)).scalar()
                update_movie.rating = ranking
                update_movie.review = review
                db.session.commit()
        return redirect("/")
    if request.method == 'GET':
        return render_template("edit.html", form=form, title=movie_title)


@app.route("/delete/<movie_title>")
def delete(movie_title):
    with app.app_context():
        db.session.delete(db.session.execute(db.select(Movies)
                                             .where(Movies.title == movie_title)).scalar())
        db.session.commit()
        return redirect("/")

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if request.method == 'GET':
        return render_template("add.html")
    if form.validate_on_submit():
        with app.app_context():
            new_movie = Movies(title=form.title.data,
                               year=form.year.data,
                               description=form.description.data,
                               rating=form.rating.data,
                               ranking=form.ranking.data,
                               review=form.review.data,
                               img_url=form.img_url.data)

            db.session.add(new_movie)
            db.session.commit()
        redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
