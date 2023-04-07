from prettytable import PrettyTable
from tabulate import tabulate
import random


def table_all(a, b):
    th = a
    td = b
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    print(table)


def table_menu(a):
    print(tabulate(a.items(), headers=['Пункт меню', "Что делает"], tablefmt='grid'))


a = random.randint(4, 7)
books_library = [("Книга_" + str(x)) for x in range(1, a)]
knig = len(books_library)
print(f'В библиотеке {knig} книг \n {books_library}')
