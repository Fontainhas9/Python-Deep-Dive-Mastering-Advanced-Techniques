def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


if __name__ == "__main__":
    # counter = count_up_to(5)
    # print(next(counter))  # 1
    # print(next(counter))  # 2

    # for num in counter:  # 3, 4, 5
    #     print(num)
    #     print(num)

    # for num in counter:
    #     print(num)

    squared_numbers = (x*x for x in range(5))
    print(next(squared_numbers))  # 0
    print(next(squared_numbers))  # 1

    for num in squared_numbers:
        print(num)
