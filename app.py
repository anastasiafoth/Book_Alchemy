from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from data_models import db, Author, Book
from datetime import datetime
import requests
from sqlalchemy import or_
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
app.secret_key = 'my_secret_key_123' # needed for redirection

db.init_app(app)

def format_date(date_string):
    """Convert a string to a datetime.date object."""
    if date_string:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    else:
        return None


def get_cover_url(title, author):
    response = requests.get(
        "https://bookcover.longitood.com/bookcover",
        params={"book_title": title, "author_name": author}
    )
    return response.json().get("url")

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']

        # request.form returns a string, needs formating
        birth_date_raw = request.form.get('birthdate')
        birth_date = format_date(birth_date_raw)

        date_of_death_raw = request.form.get('date_of_death')
        date_of_death = format_date(date_of_death_raw)

        new_author = Author(author_name=name,
                            birth_date=birth_date,
                            date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()


        flash('Author has been successfully added.', 'success')

        # Redirect, so that the form is empty again
        return redirect(url_for('add_author'))

    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    authors = Author.query.order_by(Author.author_name).all()

    if request.method == 'POST':
        title = request.form['title']
        isbn = request.form['isbn']
        year_raw = request.form.get('publication_year')
        publication_year = int(year_raw) if year_raw else None

        author_id = int(request.form['author_id'])

        new_book = Book(title=title,
                        isbn=isbn,
                        publication_year=publication_year,
                        author_id=author_id)
        db.session.add(new_book)
        db.session.commit()


        flash('Book has been successfully added.', 'success')

        # Redirect, so that the form is empty again
        return redirect(url_for('add_book'))

    return render_template('add_book.html', authors=authors)


@app.route('/')
def home():
    # Sorting
    sort = request.args.get('sort')
    direction = request.args.get('direction', 'asc')
    search_query = request.args.get('search')

    # Join needed for query
    query = Book.query.join(Author)

    # Search
    if search_query:
        search_query = search_query.strip()
        query = query.filter(
            or_(
            Book.title.like(f'%{search_query}%'),
            Author.author_name.like(f'%{search_query}%')
        ))

    # Sort
    if sort == 'title':
        query = query.order_by(
            Book.title.desc() if direction == 'desc'
            else Book.title.asc()
        )

    elif sort == 'author':
        query = query.order_by(
            Author.author_name.desc() if direction == 'desc'
            else Author.author_name.asc()
        )

    books = query.all()

    # Gets the cover for each book
    for book in books:
        book.cover_url = get_cover_url(
            book.title, book.author.author_name
        )

    return render_template('home.html', books=books)


# Creates all tables once
"""with app.app_context():
  db.create_all()"""