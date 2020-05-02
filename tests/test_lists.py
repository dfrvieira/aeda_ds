import unittest

class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SingleLinkedList()


class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoubleLinkedList()
        

if __name__ == "__main__":
    unittest.main()

