class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


if __name__ == "__main__":
    s1 = Student(name="John", grade=7)
    s2 = Student(name="Tom", grade=9)

    print(f"John is in the same grade as Tom: {s1==s2}")
