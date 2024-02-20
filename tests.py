import pytest

from conftest import fantasy_book, detective_book, child_book, comedy_book, horror_book


class TestBooksCollector:

    #проверка добавления книг в список
    def test_add_new_book_add_five_books_successfully(self, object):
        object.add_new_book(fantasy_book)
        object.set_book_genre(fantasy_book, 'Фантастика')
        assert len(object.get_books_genre()) == 1

    #проверка добавления книг с одинаковым названием в список
    def test_add_new_book_add_similar_books(self, object):
        object.add_new_book(fantasy_book)
        object.add_new_book(fantasy_book)

        assert len(object.get_books_genre()) == 1

    # проверка добавления книг с названием более 40 символов в список
    def test_add_new_book_add_books_more_than_40_symbols(self, object):
        name = 'Что делать, если ваш кот хочет вас убить убить убить убить убить убить убить убить убить убить'
        object.add_new_book(name)

        assert len(object.get_books_genre()) == 0

    # проверка, что книги добавляются без жанра
    def test_add_new_book_add_books_without_genre(self, object):
        object.add_new_book(fantasy_book)
        assert object.get_books_genre().get(fantasy_book) == ''

    # проверка установления жанра книги
    def test_set_book_genre_get_genre_successfully(self, object, prepare_books):
        assert object.get_book_genre(fantasy_book) == 'Фантастика'

    # проверка вывода списка книг с определенным жанром
    def test_get_books_with_specific_genre_five_books_get_list_genre(self, object, prepare_books):
        genre = 'Ужасы'
        assert object.get_books_with_specific_genre(genre) == [horror_book]

    # проверка вывода списка книг, которые подходят детям
    def test_get_books_for_children_five_books_get_list_book(self, object, prepare_books):
        assert object.get_books_for_children() == [fantasy_book, child_book, comedy_book]

    #один тест с параметризацией, чтобы выполнить задание, однако я везде пользуюсь фикстурой prepare_books для удобства
    @pytest.mark.parametrize(
        'book, expected_result',
        [
            (fantasy_book, True),
            (horror_book, False),
            (detective_book, False),
            (child_book, True),
            (comedy_book, True),
        ]
    )
    # проверка что в списке книг для детей нет книг для взрослых
    def test_get_books_for_children_adult_books_not_included_the_list(self, object, prepare_books, book, expected_result):
        children_books = object.get_books_for_children()
        assert (book in children_books) == expected_result

    # проверка добавления книги в избранное
    def test_add_book_in_favorites_add_one_books_successfully(self, object, prepare_books):
        object.add_book_in_favorites(fantasy_book)
        assert object.get_list_of_favorites_books() == [fantasy_book]

    # проверка, что нельзя добавить книгу дважды в избранное
    def test_add_book_in_favorites_same_books(self, object, prepare_books):
        object.add_book_in_favorites(fantasy_book)
        object.add_book_in_favorites(fantasy_book)

        assert len(object.get_list_of_favorites_books()) == 1

    # проверка, что нельзя добавить книгу не из списка books_genre
    def test_add_to_favorites_unlisted_books(self, object, prepare_books):
        object.add_book_in_favorites('Телефонный телефон')
        assert len(object.get_list_of_favorites_books()) == 0

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites_removes_book_successfully(self, object, prepare_books):
        object.add_book_in_favorites(fantasy_book)
        object.delete_book_from_favorites(fantasy_book)

        assert object.get_list_of_favorites_books() == []
