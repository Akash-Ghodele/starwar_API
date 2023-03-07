"""
whenever we are doing compute intensive operation - multi-processing

"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"[ INFO ] total time to execute :: {end}")
        return result

    return wrapper


def some_heavy_work(range_):
    return [i ** 2 for i in range(range_)]


@timeit
def main():
    ranges = [100000010, 100000020, 100000030, 100000040, 100000050, 100000060,
              100000710, 100000420, 100000530, 100000240, 100000350, 100000160]

    for range_ in ranges:
        some_heavy_work(range_)


if __name__ == "__main__":
    main()
