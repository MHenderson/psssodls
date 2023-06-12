import unittest

from psssodls.constraints import ell, ellell
from psssodls.constraints import alldiff
from psssodls.constraints import sumgeq, sumleq, pandiagonal_sum_a, psumg

class ellTests(unittest.TestCase):
    def test_ell(self):
        """Test ell constraint"""
        self.assertEqual(ell([1, 2]), 'l[1,2]')

class ellellTests(unittest.TestCase):
    def test_ell_ell(self):
        """Test ellell constraint"""
        self.assertEqual(ellell([[1, 2], [1, 3]]), '[l[1,2],l[1,3]]')

class alldiffTests(unittest.TestCase):
    def test_alldiff(self):
        """Test alldiff constraint"""
        self.assertEqual(alldiff([1, '_']), 'alldiff(l[1,_])')

class SumGeqTests(unittest.TestCase):
    def test_sumgeq(self):
        """Test sumgeq constraint"""
        self.assertEqual(sumgeq(1, 2), 'sumgeq([1],2)\n')

class SumLeqTests(unittest.TestCase):
    def test_sumleq(self):
        """Test sumleq constraint"""
        self.assertEqual(sumleq(1, 2), 'sumleq([1],2)\n')

class PandiagonalTests(unittest.TestCase):
    def test_pandiagonal(self):
        """Simple Tests"""
        p = psumg(8, 3, pandiagonal_sum_a)
        self.assertEqual(p, "sumgeq([l[0,3],l[1,4],l[2,5],l[3,6],l[4,7],l[5,0],l[6,1],l[7,2]],28)\n")
 