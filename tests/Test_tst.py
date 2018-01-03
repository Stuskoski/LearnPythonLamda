import unittest


class MyTestCase(unittest.TestCase):

    def test_default_greeting_set(self):
        self.assertEqual(2, (1 + 1))

    def test_fail(self):
        self.assertTrue('foo'.isupper())


if __name__ == '__main__':

    unittest.main()
