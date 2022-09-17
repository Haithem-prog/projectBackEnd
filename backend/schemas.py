from decimal import Decimal
from ninja import Schema

class AuthorSchema(Schema):  # showed within book
    name: str


class GenreSchema(Schema):  # showed within book
    name: str


class GenresSchemaOut(Schema):  # showed in search default
    name: str
    genresImageUrl: str

class AuthorsSchemaOut(Schema):  # showed in search default
    name: str
    authorImageUrl: str


class BookSchema(Schema):
    name: str
    bookImageUrl: str
    description: str
    price: Decimal
    rate: Decimal
    pages: int
    language: str
    total_sales: int


class BookSchemaOut(BookSchema):
    id: int
    genre: GenreSchema
    author: AuthorSchema


class BookSchemaIn(BookSchema):  # testing
    genre_id: int
    author_id: int


class ItemsSchemaOut(Schema):
    book: BookSchemaOut
    qty: int


class ItemsSchemaIn(Schema):
    user_id: int
    book_id: int
    qty: int
    removeFromCart: bool


class SavedBookSchemaOut(Schema):
    book: BookSchemaOut


class ErrorMesssage(Schema):
    detail:str
