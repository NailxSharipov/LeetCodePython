import unittest
from task_64 import Task64  # assuming the class is in a file named task62.py


class TestTask64(unittest.TestCase):
    def test_0(self):
        data = [
            [1, 3, 1], [1, 5, 1], [4, 2, 1]
        ]
        task = Task64()

        result = task.minPathSum(grid=data)
        self.assertEqual(result, 7)

    def test_1(self):
        data = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        task = Task64()
        result = task.minPathSum(grid=data)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
