from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
      return f"{self.book_name} - {self.author}"


@app.route('/')
def index():
    return 'Hello!'

# Get all the Books List
@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {
                "id": book.id,
                "book_name": book.book_name,
                "author": book.author,
                "publisher": book.publisher
            }
        output.append(book_data)

    return {"books": output}

# Get Book By ID
@app.route('/books/<int:id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {
        "book_name": book.book_name,
        "author": book.author,
        "publisher": book.publisher
    }

# Add Book
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher']
    )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# Edit Book
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']
    db.session.commit()
    return {'message': 'Book updated successfully!'}

# Delete Book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}, 404
    
    db.session.delete(book)
    db.session.commit()
    return {"message": "Deleted successfully!"}, 200

if __name__ == '__main__':
        app.run()
