from multiprocessing import Process, Pool, cpu_count
import time


def f(name):
    time.sleep(1)
    print('hello', name)


def square(n):
    return n*n


if __name__ == '__main__':
    #    p1 = Process(target=f, args=('bob',))
    #    p1.start()

    #    p2 = Process(target=f, args=('sally', ))
    #    p2.start()

    data = [1, 2, 3, 4, 5]
    pool = Pool()

    results = pool.map(square, data)

    pool.close()
    pool.join()

    print(f"Squared numbers: {results}")

    num_cores = cpu_count()
    print(f"Number of cores: {num_cores}")
