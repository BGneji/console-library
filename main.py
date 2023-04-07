from Reader import Reader
from Books import Books
from func_q import table_menu


while True:

    a = {
        "1": "Посмотреть книги в библиотеке",
        "2": "Читатель + книга посомтреть",
        "3": "Посмотреть читательский билет",
        "4": "Добавить читательский билет",
        "5": "Взять книгу из библиотеки",
        "6": "Вернуть книгу в библиотеку",
        "7": "Количество книг в библиотеке",
        "8": "Удалить читательский билет",
        "15": "Выход"
         }
    print("#" * 20)
    table_menu(a)
    user = input('Введите цифру: ')
    try:
        int(user)
        user = int(user)
    except ValueError:
        print("Введенный пункт должен быть числом")
    if user == 2:
        Reader().print_reader_book()
    elif user == 1:
        Books().info()
    elif user == 3:
        Reader().info_reader()
    elif user == 4:
        Reader().add_reader()
    elif user == 5:
        Reader().take_book()
        # print('#Читатель + книга')
    elif user == 6:
        Reader().return_reader_book()
        # Читатель - книга
    elif user == 7:
        print(Books().all_books())
        # количество книг в библиотеке
    elif user == 8:
        Reader().del_reader()
        # Читательский билет удалить
    elif user == 15:
        break
