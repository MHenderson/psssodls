"""
Unit testing of the automatic batch processing application
"""
import unittest
import psssodls
 
class PandiagonalTests(unittest.TestCase):
    def test_pandiagonal(self):
        """Simple Tests"""
        p = psssodls.psumg(8, 3, psssodls.pandiagonal_sum_a)
        self.assertEqual(p, "sumgeq([l[0,3],l[1,4],l[2,5],l[3,6],l[4,7],l[5,0],l[6,1],l[7,2]],28)\n")
 
def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(PandiagonalTests('test_pandiagonal'))
    return _suite
