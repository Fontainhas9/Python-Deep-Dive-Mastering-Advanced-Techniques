class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def __str__(self):
        return f"'{self.title}' by {self.author}"


if __name__ == '__main__':
    book = Book("1984", "George Orwell")
    print(repr(book))  # Book ('1984', 'George Orwell')

    print(eval(repr(book)).title)
    print(str(book))  # ' 1984' by George Orwell
