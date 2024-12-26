from fastapi.testclient import TestClient
from books import app

client = TestClient(app)


def test_view_all_books():
  response = client.get("/view-all-books")
  assert response.status_code == 200
  # assert the response data is as expected

def test_add_book_success():
  # create a new book data
  new_book = {
      "title": "The Hitchhiker's Guide to the Galaxy",
      "author": "Douglas Adams",
      "year": 1979,
      "available": True
  }
  response = client.post("/add-book", json=new_book)
  assert response.status_code == 200

  # check if the book is added to the BOOKS list
  # ...

def test_add_book_fail_without_required_fields():
  # create a new book data without required fields
  new_book = {
      "author": "Douglas Adams",
      "year": 1979,
      "available": True
  }
  response = client.post("/add-book", json=new_book)
  assert response.status_code == 422  # Unprocessable Entity

def test_view_only_available_books():
  response = client.get("/view-only-available_books")
  assert response.status_code == 200
  # assert the response data contains only available books

def test_borrow_available_books_success():
  # find the id of an available book
  book_id = 1  # assuming the first book is available
  response = client.get("/borrow-available-books/{}".format(book_id))
  assert response.status_code == 200

  # check if the book is marked as unavailable
  # ...

def test_borrow_unavailable_books():
  # find the id of an unavailable book
  book_id = 1  # assuming the first book is already borrowed
  response = client.get("/borrow-available-books/{}".format(book_id))
  assert response.status_code == 404  # Not Found

def test_return_borrowed_books():
  response = client.get("/return-borrowed-books/")
  assert response.status_code == 200
  # assert the response data contains only borrowed books