import peewee

from repository.library import Library

if __name__ == '__main__':
    try:

        library = Library()
        library.connect()

        print(library.count())
        print(library.get_at(1))
        print(library.get_all_books())

        library.close()

    except peewee.InternalError as px:
        print(str(px))
