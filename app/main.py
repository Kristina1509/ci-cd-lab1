
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Book Management API",
    description="REST API для керування книгами",
    version="1.0.0",
)


class Book(BaseModel):
    title: str
    author: str
    year: int


books = {}
next_id = 1


@app.get("/api/items")
def get_books():
    """Отримати список усіх книг."""
    return list(books.values())


@app.get("/api/items/{book_id}")
def get_book(book_id: int):
    """Отримати книгу за ідентифікатором."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    return books[book_id]


@app.post("/api/items", status_code=201)
def create_book(book: Book):
    """Створити нову книгу."""
    global next_id

    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
    }

    books[next_id] = new_book
    next_id += 1

    return new_book


@app.put("/api/items/{book_id}")
def update_book(book_id: int, book: Book):
    """Оновити наявну книгу."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    updated_book = {
        "id": book_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
    }

    books[book_id] = updated_book
    return updated_book


@app.delete("/api/items/{book_id}", status_code=204)
def delete_book(book_id: int):
    """Видалити книгу."""
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    del books[book_id]
    return None
