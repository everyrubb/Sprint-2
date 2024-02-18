import pytest


class TestBooksCollector:

    #проверка добавления книг в список
    def test_add_new_book_add_five_books(self, object, prepare_books):
        assert len(object.get_books_genre()) == 5

    #проверка добавления книг с одинаковым названием в список
    def test_add_new_book_add_similar_books(self, object):
        object.add_new_book('Что делать, если ваш кот хочет вас убить')
        object.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(object.get_books_genre()) == 1

    # проверка добавления книг с названием более 40 символов в список
    def test_add_new_book_add_books_more_than_40_symbols(self, object):
        name = 'Что делать, если ваш кот хочет вас убить убить убить убить убить убить убить убить убить убить'
        object.add_new_book(name)

        assert len(object.get_books_genre()) == 0

    # проверка, что книги добавляются без жанра
    def test_add_new_book_add_books_without_genre(self, object):
        name = 'Что делать, если ваш кот хочет вас убить'
        object.add_new_book(name)

        assert object.get_books_genre().get(name) == ''

    # проверка установления жанра книги
    def test_set_book_genre_get_genre(self, object, prepare_books):
        name = 'Что делать, если ваш кот хочет вас убить'
        assert object.get_book_genre(name) == 'Фантастика'

    # проверка вывода списка книг с определенным жанром
    def test_get_books_with_specific_genre_five_books_get_list_genre(self, object, prepare_books):
        genre = 'Ужасы'
        assert object.get_books_with_specific_genre(genre) == ['Гордость и предубеждение и зомби', 'Шурик Хомлс и Воланд']

    # проверка вывода списка книг, которые подходят детям
    def test_get_books_for_children_five_books_get_list_book(self, object, prepare_books):
        assert object.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить', 'Колобок', 'Три дома']

    #один тест с параметризацией, чтобы выполнить задание, однако я везде пользуюсь фикстурой prepare_books для удобства
    @pytest.mark.parametrize(
        'book, genre',
        [
            ("Что делать, если ваш кот хочет вас убить", "Фантастика"),
            ("Гордость и предубеждение и зомби", "Ужасы"),
            ("Шурик Хомлс и Воланд", "Ужасы"),
            ("Колобок", "Мультфильмы"),
            ("Три дома", "Комедии"),
        ]
    )
    # проверка что в списке книг для детей нет книг для взрослых
    def test_get_books_for_children_adult_books_not_included_the_list(self, object, book, genre):
        object.add_new_book(book)
        object.add_new_book(genre)

        assert 'Гордость и предубеждение и зомби' and 'Шурик Хомлс и Воланд' not in object.get_books_for_children()

    # проверка добавления книги в избранное
    def test_add_book_in_favorites_add_one_books(self, object, prepare_books):
        name = 'Колобок'
        object.add_book_in_favorites(name)

        assert object.get_list_of_favorites_books() == [name]

    # проверка удаления книги из избранного
    def test_delete_book_from_favorites_remove_one_books(self, object, prepare_books):
        name = 'Три дома'
        object.add_book_in_favorites(name)
        object.delete_book_from_favorites(name)

        assert object.get_list_of_favorites_books() == []