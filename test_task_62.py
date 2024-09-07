import unittest
from task_62 import Task62  # assuming the class is in a file named task62.py

class TestTask62(unittest.TestCase):
    def test_0(self):
        result = Task62.unique_paths(3, 7)
        self.assertEqual(result, 28)

    def test_1(self):
        result = Task62.unique_paths(3, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
