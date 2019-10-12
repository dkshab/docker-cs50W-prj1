# services/users/project/api/models.py

from sqlalchemy.sql import func

from project import db


class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    isbn = db.Column(db.String(128), nullable=False)

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn
        }
