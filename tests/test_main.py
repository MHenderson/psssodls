import unittest

from psssodls.main import begin, end
from psssodls.main import box_constraints_str, latin_constraints_str, orthogonality_constraints_str, pandiagonality_constraints_str, strongly_symmetric_constraints_str
from psssodls.main import psssodls_string

class BeginTests(unittest.TestCase):
    def test_begin(self):
        """Test begin"""
        self.assertEqual(begin(1), 'MINION 3\n\n**VARIABLES**\nDISCRETE l[1,1] {0..0}\n\n**SEARCH**\nPRINT ALL\n\n**CONSTRAINTS**\n\n')

class EndTests(unittest.TestCase):
    def test_end(self):
        """Test end"""
        self.assertEqual(end(), '**EOF**')

class LatinConstraintsStrTests(unittest.TestCase):
    def test_latin_constraints_str(self):
        """Test latin constraints string"""
        self.assertEqual(latin_constraints_str(1), '# Latin constraints. \n\nalldiff(l[0,_])\nalldiff(l[_,0])\n\n')

class BoxConstraintsStrTests(unittest.TestCase):
    def test_box_constraints_str(self):
        """Test box constraints string"""
        self.assertEqual(box_constraints_str(1), '# Box constraints. \n\nalldiff([l[0,0]])\n\n')

class PandiagonalityConstraintsStrTests(unittest.TestCase):
    def test_pandiagonality_constraints_str(self):
        """Test pandiagonality constraints string"""
        self.assertEqual(pandiagonality_constraints_str(1), '# Pandiagonality constraints. \n\nsumgeq([l[0,0]],0)\nsumleq([l[0,0]],0)\nsumgeq([l[0,0]],0)\nsumleq([l[0,0]],0)\n\n')

class StronglySymmetricConstraintsStrTests(unittest.TestCase):
    def test_strongly_symmetric_constraints_str(self):
        """Test strongly symmetric constraints string"""
        self.assertEqual(strongly_symmetric_constraints_str(1), '# Strongly symmetric constraints. \n\nsumgeq([l[0,0],l[0,0]], 0)\nsumleq([l[0,0],l[0,0]], 0)\n\n')

class OrthogonalityConstraintsStrTests(unittest.TestCase):
    def test_orthogonality_constraints_str(self):
        """Test orthogonality constraints string"""
        self.assertEqual(orthogonality_constraints_str(1), '# Orthogonality constraints. \n\n\n')

class PsssodlsStringTests(unittest.TestCase):
    def test_psssodls_string(self):
        """Test main psssodls string function"""
        self.assertEqual(psssodls_string(1, False), 'MINION 3\n\n**VARIABLES**\nDISCRETE l[1,1] {0..0}\n\n**SEARCH**\nPRINT ALL\n\n**CONSTRAINTS**\n\n# Latin constraints. \n\nalldiff(l[0,_])\nalldiff(l[_,0])\n\n# Pandiagonality constraints. \n\nsumgeq([l[0,0]],0)\nsumleq([l[0,0]],0)\nsumgeq([l[0,0]],0)\nsumleq([l[0,0]],0)\n\n# Strongly symmetric constraints. \n\nsumgeq([l[0,0],l[0,0]], 0)\nsumleq([l[0,0],l[0,0]], 0)\n\n# Orthogonality constraints. \n\n\n**EOF**')
        self.assertEqual(psssodls_string(1, True),  'MINION 3\n\n**VARIABLES**\nDISCRETE l[1,1] {0..0}\n\n**SEARCH**\nPRINT ALL\n\n**CONSTRAINTS**\n\n# Latin constraints. \n\nalldiff(l[0,_])\nalldiff(l[_,0])\n\n# Box constraints. \n\nalldiff([l[0,0]])\n\n# Pandiagonality constraints. \n\nsumgeq([l[0,0]],0)\nsumleq([l[0,0]],0)\nsumgeq([l[0,0]],0)\nsumleq([l[0,0]],0)\n\n# Strongly symmetric constraints. \n\nsumgeq([l[0,0],l[0,0]], 0)\nsumleq([l[0,0],l[0,0]], 0)\n\n# Orthogonality constraints. \n\n\n**EOF**')