import unittest

from psssodls.constraints import ell, ellell
from psssodls.constraints import alldiff, vecneq
from psssodls.constraints import sdk_positions_box
from psssodls.constraints import sumgeq, sumleq
from psssodls.constraints import psumg, psuml
from psssodls.constraints import pandiagonal_sum_a, pandiagonal_sum_b

class EllTests(unittest.TestCase):
    def test_ell(self):
        """Test ell constraint"""
        self.assertEqual(ell([1, 2]), 'l[1,2]')

class EllellTests(unittest.TestCase):
    def test_ell_ell(self):
        """Test ellell constraint"""
        self.assertEqual(ellell([[1, 2], [1, 3]]), '[l[1,2],l[1,3]]')

class AlldiffTests(unittest.TestCase):
    def test_alldiff(self):
        """Test alldiff constraint"""
        self.assertEqual(alldiff([1, '_']), 'alldiff(l[1,_])')

class VecNeqTests(unittest.TestCase):
    def test_vecneq(self):
        """Test vecneq constraint"""
        self.assertEqual(vecneq([[1, 2], [1, 3]], [[1, 2], [1, 3]]), 'watchvecneq([l[1,2],l[1,3]], [l[1,2],l[1,3]])')

class SdkPositionsBoxTests(unittest.TestCase):
    def test_sdk_positions_box(self):
        """Test sdk_positions_box"""
        self.assertEqual(sdk_positions_box(1, 2, 3), [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)])

class PandiagonalSumATests(unittest.TestCase):
    def test_pandiagonal_sum_a(self):
        """Test pandiagonal_sum_a"""
        self.assertEqual(psumg(8, 3, pandiagonal_sum_a), "sumgeq([l[0,3],l[1,4],l[2,5],l[3,6],l[4,7],l[5,0],l[6,1],l[7,2]],28)\n")

class PandiagonalSumBTests(unittest.TestCase):
    def test_pandiagonal_sum_b(self):
        """Test pandiagonal_sum_b"""
        self.assertEqual(psumg(8, 3, pandiagonal_sum_b), "sumgeq([l[0,3],l[1,2],l[2,1],l[3,0],l[4,7],l[5,6],l[6,5],l[7,4]],28)\n")

class SumGeqTests(unittest.TestCase):
    def test_sumgeq(self):
        """Test sumgeq constraint"""
        self.assertEqual(sumgeq(1, 2), 'sumgeq([1],2)\n')

class SumLeqTests(unittest.TestCase):
    def test_sumleq(self):
        """Test sumleq constraint"""
        self.assertEqual(sumleq(1, 2), 'sumleq([1],2)\n')

class PsumgTests(unittest.TestCase):
    def test_psumg(self):
        """Test psumg constraint"""
        self.assertEqual(psumg(3, 0, pandiagonal_sum_a), 'sumgeq([l[0,0],l[1,1],l[2,2]],3)\n')

class PsumlTests(unittest.TestCase):
    def test_psuml(self):
        """Test psuml constraint"""
        self.assertEqual(psuml(3, 0, pandiagonal_sum_a), 'sumleq([l[0,0],l[1,1],l[2,2]],3)\n')