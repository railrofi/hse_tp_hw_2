from unittest import TestCase, main
from tz2 import _max, _min, _sum, _mult

testlist = [1, 3, 42, 52, 525, 74, 3, 0, 1, -1, -123414, 32325]


class Test(TestCase):

    def test_max(self):
        self.assertEqual(_max(testlist), 32325)

    def test_min(self):
        self.assertEqual(_min(testlist), -123414)

    def test_mult(self):
        self.assertEqual(_mult(testlist), 0)

    def test_sum(self):
        self.assertEqual(_sum(testlist), -90389)

    def test_my(self):
        self.assertGreaterEqual(_max(testlist), _min(testlist))


if __name__ == '__main__':
    main()
