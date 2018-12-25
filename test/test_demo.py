import unittest

from interpRelation import demo

class DemoTest(unittest.TestCase):

    def test_all(self):
        d = demo.Demo()
        filename = 'demo.py'
        d.start(filename)
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()