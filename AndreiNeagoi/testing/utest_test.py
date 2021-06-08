import unittest
from unittest import result
import utest


class TestMain(unittest.TestCase):

    def test_do_stuff(self):
        test_param = 10
        result = utest.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sfsd'
        result = utest.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = utest.do_stuff(test_param)
        self.assertEqual(result, 'please try again')

    def test_do_stuff4(self):
        test_param = ''
        result = utest.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff5(self):
        test_param = 0
        result = utest.do_stuff(test_param)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
