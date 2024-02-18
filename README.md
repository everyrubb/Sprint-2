# Sprint#2

### Описание проекта

Приложение BooksCollector позволяет добавлять книги в список, устанавливать жанр книги, сортировать книги по возрастному ограничению, добавлять книгу в избранное и удалять.

### Структура проекта

1. Класс ```BooksCollector``` располагается в файле ```main.py```
2. Тесты распологаются в файле ```tests.py```
3. Фикстуры распологаются в файле ```conftest.py```

### Методы класса BooksCollector и их тестовое покрытие

| Метод        |                                                                       Описание метода                                                                        |                                                                                                                                                                                                                      Проверка метода |
| ------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| ```add_new_book```    | Добавляет новую книгу в словарь без указания жанра.<br/> Название книги может содержать максимум 40 символов. <br/> Дважды одну и ту же книгу добавить нелья |                                                                ```test_add_new_book_add_five_books_successfully``` <br/> ```test_add_new_book_add_books_more_than_40_symbols``` <br/>```test_add_new_book_add_books_without_genre``` |
| ```set_book_genre```      |                             Устанавливает жанр книги, если книга есть в ```books_genre``` и её жанр входит в список ```genre```.                             |                                                                                                                                                                                     ```test_set_book_genre_get_genre_successfully``` |
| ```get_book_genre```   |                                                               Выводит жанр книги по её имени.                                                                |                                                                                                                                                                                     ```test_set_book_genre_get_genre_successfully``` |
| ```get_books_with_specific_genre```   |                                                          Выводит список книг с определённым жанром.                                                          |                                                                                                                                                                   ```test_get_books_with_specific_genre_five_books_get_list_genre``` |
| ```get_books_genre```   |                                                          Выводит текущий словарь ```books_genre```.                                                          |                   ```test_add_new_book_add_five_books_successfully```<br/>```test_add_new_book_add_similar_books``` <br/>```test_add_new_book_add_books_more_than_40_symbols```<br/> ```test_add_new_book_add_books_without_genre``` |
| ```get_books_for_children```   |                              Возвращает книги, которые подходят детям. <br/> У жанра книги не должно быть возрастного рейтинга.                              |                                                                                                 ```test_get_books_for_children_five_books_get_list_book``` <br/> ```test_get_books_for_children_adult_books_not_included_the_list``` |
| ```add_book_in_favorites```   |          Добавляет книгу в избранное. <br/> Книга должна находиться в словаре ```books_genre```. <br/> Повторно добавить книгу в избранное нельзя.           | ```test_add_book_in_favorites_add_one_books_successfully``` <br/> ```test_add_book_in_favorites_same_books``` <br/> ```test_add_to_favorites_unlisted_books``` <br/> ```test_delete_book_from_favorites_removes_book_successfully``` |
| ```delete_book_from_favorites```   |                                                       Удаляет книгу из избранного, если она там есть.                                                        |                                                                                                                                                                      ```test_delete_book_from_favorites_removes_book_successfully``` |
| ```get_list_of_favorites_books```   |                                                               Получает список избранных книг.                                                                |                   ```test_add_book_in_favorites_same_books``` <br/> ```test_add_to_favorites_unlisted_books``` <br/> ```test_delete_book_from_favorites_removes_book_successfully``` <br/> ```test_add_book_in_favorites_add_one_books_successfully``` |

### Запуск тестов в проекте

Запустить тесты из терминала можно такой командой:

```pytest -v tests.py```