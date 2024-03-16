import pytest

from main import BooksCollector


@pytest.fixture(scope="function")
def object():
    collector = BooksCollector()
    return collector

fantasy_book = 'Что делать, если ваш кот хочет вас убить'
horror_book = 'Гордость и предубеждение и зомби'
detective_book = 'Шурик Хомлс и Воланд'
child_book = 'Колобок'
comedy_book = 'Три дома'

@pytest.fixture(scope="function")
def prepare_books(object):
    books_genre = [
        (fantasy_book, "Фантастика"),
        (horror_book, "Ужасы"),
        (detective_book, "Детективы"),
        (child_book, "Мультфильмы"),
        (comedy_book, "Комедии"),
    ]

    for book, genre in books_genre:
        object.add_new_book(book)
        object.set_book_genre(book, genre)