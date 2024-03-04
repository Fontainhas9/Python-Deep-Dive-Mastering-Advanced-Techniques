class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)


if __name__ == '__main__':
    lib = Library(books=['book1', 'book2'])
    print(len(lib))
