from Books import Books
from tabulate import tabulate
from prettytable import PrettyTable
from func_q import *




class Reader:
    def __init__(self, list_reader=[], reader_book={}):
        self.reader = list_reader
        self.reader_book = reader_book

    def __str__(self):
        return f'{self.reader}'

    def info_reader(self):
        th = ["Читатели"]
        td = self.reader
        table_all(th, td)
        # columns = len(th)
        # table = PrettyTable(th)
        # td_data = td[:]
        # while td_data:
        #     table.add_row(td_data[:columns])
        #     td_data = td_data[columns:]
        # print(table)

    def add_reader(self):
        add_fio = input('Введите ФИО для читательского билета: ')
        try:
            float(add_fio)
            print('Должно быть строка')
        except ValueError:
            self.reader.append(str(add_fio))
            print('Читательский билет добавлен')
            return self.reader

    def del_reader(self):
        del_fio = input('Введите ФИО для читательского билета для удаления: ')
        try:
            self.reader.remove(del_fio)
            print('Читательский билет удален')
            return self.reader
        except:
            print('Такого читательского билета нет!')

    def take_book(self):
        if not self.reader:
            print('Не один читатель не зарегистрирован')
        else:
            print(Reader())
            chit = input("ФИО читателя: ")

            if chit in self.reader:
                if chit not in self.reader_book:
                    a = Books().del_book()
                    self.reader_book[chit] = list()
                    self.reader_book[chit].append(a)
                    return self.reader_book
                else:
                    a = Books().del_book()
                    self.reader_book[chit].append(a)
                    return self.reader_book
            elif chit not in self.reader:
                print('Такого читательского билета нет')

    def print_reader_book(self):
        print(tabulate(self.reader_book.items(), headers=['Читатель', "Книги"], tablefmt='grid'))

    def return_reader_book(self):
        allnumber_books = Books().all_books()
        if allnumber_books == knig:
            # print(knig)
            return print('В библиотеке все книги')

        chit_add = input("ФИО читателя: ")
        for j in self.reader:
            if j == chit_add:
                print(f'{self.reader_book[chit_add]}')
                book_add = input('Введите название книги у читателя: ')
                for items_book1 in self.reader_book[chit_add]:
                    print(items_book1)
                    if items_book1 == [book_add]:
                        Books().add_books(''.join(items_book1))
                        self.reader_book[chit_add].remove([book_add])
                        print('Книга возвращена в библиотеку')
                        return self.reader_book



