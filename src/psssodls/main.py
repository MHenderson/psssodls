"""
Python package `psssodls` generates Minion 3 input files
for pandiagonal strongly symmetric self-orthogonal diagonal
latin squares (PSSSODLS).
"""

import sys

from math import sqrt

def begin(n):
  return """\
MINION 3

**VARIABLES**
DISCRETE l[{},{}] {{0..{}}}

**SEARCH**
PRINT ALL

**CONSTRAINTS**

""".format(n, n, n - 1)

def end():
  return "**EOF**"

def pandiagonality_constraints_str(n):
  """Returns a string containing the pandiagonality constraints for a square
  of size n."""
  s = '# Pandiagonality constraints. \n\n'
  for w in range(n):
    s += psumg(n, w, pandiagonal_sum_a)
    s += psuml(n, w, pandiagonal_sum_a)
    s += psumg(n, w, pandiagonal_sum_b)
    s += psuml(n, w, pandiagonal_sum_b)
    s += '\n'
  return s

def strongly_symmetric_constraints_str(n):
  s = '# Strongly symmetric constraints. \n\n'
  for i in range(n):
    for j in range(n):
      s += 'sumgeq({}, {})\n'.format(ellell([[i,j],[n - 1 - i, n - 1 - j]]), n - 1)
      s += 'sumleq({}, {})\n'.format(ellell([[i,j],[n - 1 - i, n - 1 - j]]), n - 1)
    s += '\n'
  return s

def orthogonality_constraints_str(n):
  """Returns a string containing the orthogonality constraints for a square
  of size n."""
  F = [[(i,j), (j,i)] for i in range(n) for j in range(n)]
  s = '# Orthogonality constraints. \n\n'
  s += "".join([vecneq(p, q) + '\n' for p in F for q in F if p > q])
  return s + '\n'

def psssodls_string(n, boxes):
  """Returns a string which is the entire Minion 3 format constraint program
  for PSSSODLS(n)."""
  s = begin(n)
  s += latin_constraints_str(n)
  if boxes:
    s += box_constraints_str(n)
  s += pandiagonality_constraints_str(n)
  s += strongly_symmetric_constraints_str(n)
  s += orthogonality_constraints_str(n)
  s += end()
  return s