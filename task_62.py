class Task62:

    @staticmethod
    def unique_paths(m: int, n: int) -> int:
        if m < 2 or n < 2:
            return 1

        array = [1] * n

        for _ in range(1, m):
            s = 1
            for x in range(1, n):
                s += array[x]
                array[x] = s

        return array[n - 1]
