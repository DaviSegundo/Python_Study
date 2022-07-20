from typing import List


class Reusable:

    def test(self):
        print(f"Using object {id(self)}")


class ReusablePool:

    def __init__(self, size) -> None:
        self.size = size
        self.free = []
        self.in_use = []

        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if len(self.free) <= 0:
            raise Exception("No more objects are available")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)


class PoolManager:

    def __init__(self, pool: ReusablePool) -> None:
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, traceback):
        self.pool.release(self.obj)


if __name__ == '__main__':
    pool = ReusablePool(2)

    with PoolManager(pool) as r:
        r.test()