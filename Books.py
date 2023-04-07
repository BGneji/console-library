from prettytable import PrettyTable
from func_q import *



class Books:

    def __init__(self, books=books_library):
        self.books = books


    def __str__(self):
        return f'{self.books}'

    def info(self):
        th = ["Книги"]
        td = self.books
        # table_all(th, td)
        columns = len(th)
        table = PrettyTable(th)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        print(table)

    def add_books(self, items_book):
        self.items_book = items_book
        self.books.append(self.items_book)
        return self.books

    def del_book(self):
        print(self.books)
        kniga_del = input('Введите название книги которую берет читатель: ')
        if kniga_del in self.books:
            self.books.remove(kniga_del)
            print('Книга взята из библиотеке')
            return [kniga_del]
        else:
            print('Такой книги нет')

    def all_books(self):
        return f'Сколько книг в библиотеке {len(self.books)}'