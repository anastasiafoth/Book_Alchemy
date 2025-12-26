from sqlite3.dbapi2 import Date

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __str__(self):
        return f"Author(author_id = {self.author_id}, \
        name = {self.author_name}, birth date = {self.birth_date}, \
        date of death = {self.date_of_death})"

    def __repr__(self):
        if not self.date_of_death:
            return f"Author: {self.author_name}, is born on {self.birth_date}."
        else:
            return f"Author: {self.author_name}, is born on {self.birth_date}\
            and died on {self.date_of_death}."


class Book(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey("authors.author_id"),
        nullable=False
    )

    author = db.relationship("Author", backref="books")

    def __str__(self):
        return f"Book(book_id = {self.book_id}, \
        title = {self.title}, isbn = {self.isbn}, \
        publication year = {self.publication_year}\
        author id = {self.author_id}"

    def __repr__(self):
        return f"The book {self.title}, is published {self.publication_year}\
            and has the ISBN {self.isbn}."


