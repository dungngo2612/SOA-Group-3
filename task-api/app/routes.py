"""HTTP routes for the Book Management API."""

from flask import Blueprint, jsonify, request

from . import services
from .schemas import parse_book_payload

books_bp = Blueprint("books", __name__)

EDITABLE_FIELDS = ("title", "author", "published_year")


def error(message, status_code):
    return jsonify({"error": message}), status_code


@books_bp.get("/")
def index():
    return jsonify({"message": "Book Management API", "books_endpoint": "/books"})


@books_bp.get("/books")
def list_books():
    books = services.list_books()
    return jsonify({"data": books, "total": len(books)}), 200


@books_bp.get("/books/<int:book_id>")
def get_book(book_id):
    book = services.get_book(book_id)
    if book is None:
        return error("Book not found", 404)
    return jsonify(book), 200


@books_bp.post("/books")
def create_book():
    payload, validation_error = parse_book_payload(EDITABLE_FIELDS)
    if validation_error:
        return error(validation_error, 400)

    # The server owns the ID; clients must not choose it.
    book = services.create_book(payload)
    return jsonify(book), 201


@books_bp.put("/books/<int:book_id>")
def update_book(book_id):
    payload, validation_error = parse_book_payload(EDITABLE_FIELDS)
    if validation_error:
        return error(validation_error, 400)

    book = services.update_book(book_id, payload)
    if book is None:
        return error("Book not found", 404)
    return jsonify(book), 200


@books_bp.delete("/books/<int:book_id>")
def delete_book(book_id):
    if not services.delete_book(book_id):
        return error("Book not found", 404)
    return "", 204
