from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_books_collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    if result.scalars == 0:
        return render_template('index.html', books='EMPTY')
    else:
        all_books = result.scalars().all()
        return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('add.html', db=db)
    else:
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        with app.app_context():
            new_book = Book(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    if request.method == "GET":
        with app.app_context():
            book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        title = book.title
        rating = book.rating
        return render_template('edit.html', id=id, title=title, rating=rating)
    else:
        new_rating = float(request.form['new_rating'])
        with app.app_context():
            book = db.get_or_404(Book, id)
            book.rating = new_rating
            db.session.commit()
        return redirect(url_for('home'))

@app.route('/delete')
def delete():
    id = request.args.get('id')
    with app.app_context():
        book = db.get_or_404(Book, id)
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
