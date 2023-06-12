import unittest

from psssodls.constraints import sumgeq, sumleq, pandiagonal_sum_a, psumg

class ConstraintTests(unittest.TestCase):
    def test_sumgeq(self):
        """Test sumgeq constraint"""
        self.assertEqual(sumgeq(1, 2), 'sumgeq([1],2)\n')

    def test_sumleq(self):
        """Test sumleq constraint"""
        self.assertEqual(sumleq(1, 2), 'sumleq([1],2)\n')

class PandiagonalTests(unittest.TestCase):
    def test_pandiagonal(self):
        """Simple Tests"""
        p = psumg(8, 3, pandiagonal_sum_a)
        self.assertEqual(p, "sumgeq([l[0,3],l[1,4],l[2,5],l[3,6],l[4,7],l[5,0],l[6,1],l[7,2]],28)\n")
 
def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(PandiagonalTests('test_pandiagonal'))
    _suite.addTest(ConstraintTests('test_sumgeq'))
    return _suite
