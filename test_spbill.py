#!/usr/bin/env python3

import unittest
import collections

from splitbill import SplitBill


class SplitBillTest(unittest.TestCase):
    def setUp(self):
        self.sb = SplitBill()
        self.csv = self.sb.open(['test_bills1.csv', 'test_bills2.csv'])
        
    def test_format_stdout(self):
        sample = collections.OrderedDict()
        sample = { 'alice': -112.5,
                   'bob': -82.5,
                   'carol': 157.5,
                   'dan': -22.5,
                   'erin': 60.0 }

        lent = self.sb.calculate(self.csv)
        self.assertEqual(sample, lent)

if __name__ == '__main__':
    unittest.main()
