import pytest


from main import BooksCollector

@pytest.fixture(scope="function")
def object():
    collector = BooksCollector()
    return collector

books_genre = [
        ("Что делать, если ваш кот хочет вас убить", "Фантастика"),
        ("Гордость и предубеждение и зомби", "Ужасы"),
        ("Шурик Хомлс и Воланд", "Ужасы"),
        ("Колобок", "Мультфильмы"),
        ("Три дома", "Комедии"),
    ]

@pytest.fixture(scope="function")
def prepare_books(object):
    for book, genre in books_genre:
        object.add_new_book(book)
        object.set_book_genre(book, genre)
    return books_genre