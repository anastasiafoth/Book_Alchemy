# Book Alchemy

A modern web application for managing your personal book collection with beautiful visual elements and powerful search capabilities.


## Features

- 📚 Add and manage books with titles, authors, and cover images
- 👥 Track author information including birth and death dates
- 🔍 Search through your collection by title or author
- 🖼️ Automatic book cover retrieval
- 🎨 Modern, responsive design with smooth animations
- 📱 Mobile-friendly interface
- 🔄 Sort books by title or author in ascending/descending order

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3 (with Flexbox and CSS Grid)
- **Database**: SQLite with SQLAlchemy ORM
- **Deployment**: (Specify if applicable)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anastasiafoth/Book_Alchemy.git
   cd Book_Alchemy
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python
   >>> from app import app, db
   >>> app.app_context().push()
   >>> db.create_all()
   >>> exit()
   ```

5. **Run the application**
   ```bash
   python -m flask run
   ```

6. **Open your browser**
   Visit `http://127.0.0.1:5000` to access the application

## Usage

1. **Add Authors**
   - Navigate to "Add Author"
   - Fill in the author's details
   - Submit the form

2. **Add Books**
   - Go to "Add Book"
   - Select an author from the dropdown
   - Enter book details
   - The system will automatically try to fetch a book cover

3. **Browse Your Collection**
   - View all books on the home page
   - Use the search bar to find specific books
   - Sort books by title or author

## Project Structure

```
 Book_Alchemy/
├── static/
│   ├── stylesheet.css
│   └── placeholder.jpg
├── templates/
│   ├── add_author.html
│   ├── add_book.html
│   └── home.html
├── data/
│   └── library.sqlite
├── app.py
├── data_models.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Book cover API provided by [BookCover API](https://bookcover.longitood.com/)
- Inspired by book lovers and collectors everywhere
