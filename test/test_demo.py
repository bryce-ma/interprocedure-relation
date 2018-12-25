import unittest
import os

from interpRelation import demo

class DemoTest(unittest.TestCase):

    def test_all(self):
        d = demo.Demo()
        filename = os.path.join(os.path.dirname(__file__), 'input.py')
        print('analyse file: ' + filename)
        d.start(filename)
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()