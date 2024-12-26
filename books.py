from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field



app = FastAPI()


class Book:
  id : int
  title : str
  author : str
  year : int
  available : bool

  def __init__(self,id,title,author,year,available):
    self.id = id
    self.title = title
    self.author = author
    self.year = year
    self.available = available



class BookRequest(BaseModel):
  id : int
  title : str = Field(min_length=3)
  author : str = Field(min_lenght=3)
  year : int 
  available : bool 



BOOKS = [
  Book(1,"Harry Potter","J.K. Rowling",1997,available=True),
  Book(2,"The Hobbit","J.R.R. Tolkien",1937,available=True),
  Book(3,"The Catcher in the Rye","J.D. Salinger",1951,available=True),
  Book(4,"To Kill a Mockingbird","Harper Lee",1960,available=True),
  Book(5,"1984","George Orwell",1949,available=True),
  Book(6,"The Great Gatsby","F. Scott Fitzgerald",1925,available=True),
  Book(7,"The Da Vinci Code","Dan Brown",2003,available=True),
  Book(8,"The Alchemist","Paulo Coelho",1988,available=True),
  Book(9,"The Little Prince","Antoine de Saint-Exupéry",1994,available=True),
  Book(10,"The Chronicles of Narnia","C.S. Lewis",1950,available=True)

]


@app.get("/view-all-books")
async def view_all_books():
  return BOOKS

@app.post("/add-book")
async def create_new_book(book_request: BookRequest):
  new_book = Book(**book_request.dict())
  BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
  if len(BOOKS)>0:
    book.id = BOOKS[-1].id+1
  
  else:
    book.id = 1

  return book

@app.get("/view-only-available-books")
async def view_only_available_books():
  available_books = []
  for BOOK in BOOKS:
    if BOOK.available is True:
      available_books.append(BOOK)
  return available_books

@app.get("/borrow-available-books/{book_id}")
async def borrow_available_books(book_id: int):
  for BOOK in BOOKS:
    if BOOK.id == book_id:
      if BOOK.available is True:
        BOOK.available = False
      else:
        raise HTTPException(status_code=404, detail="Book is not available")
    
@app.get("/return-borrowed-books/")
async def return_borrowed_books():
  borrowed_books = []
  for BOOK in BOOKS:
    if BOOK.available is True:
      borrowed_books.append(BOOK)
  return borrowed_books


  





