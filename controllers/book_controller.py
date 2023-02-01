from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book
from models.author import Author

book_blueprint = Blueprint("book", __name__)


@book_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)


@book_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)


@book_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    book = Book(title, author, genre)
    book_repository.save(book)
    return redirect("/books")


@book_blueprint.route("/books/<id>", methods=["GET"])
def show_book(id):
    authors = author_repository.select_all()
    book = book_repository.select(id)
    return render_template("books/show.html", show_book=book, authors=authors)


@book_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
