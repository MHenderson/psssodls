#!/usr/bin/env python

import sys

def ell(p):
  """This function takes a pair p = [p[0], p[1]] and returns the string
  'l[p[0],p[1]]'."""
  return 'l[' + str(p[0]) + ',' + str(p[1]) + ']'

def ellell(p):
  return '[' + ell(p[0]) + ',' + ell(p[1]) + ']'

def alldiff(p):
  """Returns a string representing an all_different constraint over the
  variables in the vector v."""
  return 'alldiff(' + ell(p) + ')'

def vecneq(p, q):
  """Returns a string representing an vectorised inequality constraint between
  the two vectors p and q."""
  return 'watchvecneq(' + ellell(p) + ',' + ellell(q) + ')'

def begin(n):
  s = \
"""
MINION 3

**VARIABLES**
DISCRETE l[%d,%d] {0..%d}

**SEARCH**
PRINT ALL

**CONSTRAINTS**
""" % (n, n, n - 1)
  return s + '\n'

def end():
  return "**EOF**"

def latin_constraints_str(n):
  """Returns a string containing the latin constraints for a square of size
  n."""
  s = '# Latin constraints. \n\n'
  s += "".join([alldiff([i,'_']) + '\n' + alldiff(['_',i]) + '\n' for i in range(n)])
  return s + '\n'

def pandiagonal_sum_a(n, w):
  return "".join([ell([i % n, (i + w) % n]) for i in range(n)])

def pandiagonal_sum_b(n, w):
  return "".join([ell([i % n, (w - i) % n]) for i in range(n)])

def pandiagonality_constraints_str(n):
  """Returns a string containing the pandiagonality constraints for a square
  of size n."""
  s = '# Pandiagonality constraints. \n\n'
  pandiagonal_sum_s = str(n*(n - 1)/2)
  for w in range(n):
    s += 'sumgeq(' + pandiagonal_sum_a(n, w) + ', ' + pandiagonal_sum_s + ')' + '\n'
    s += 'sumleq(' + pandiagonal_sum_a(n, w) + ', ' + pandiagonal_sum_s + ')' + '\n'
    s += 'sumgeq(' + pandiagonal_sum_b(n, w) + ', ' + pandiagonal_sum_s + ')' + '\n'
    s += 'sumleq(' + pandiagonal_sum_b(n, w) + ', ' + pandiagonal_sum_s + ')' + '\n\n'
  return s

def strongly_symmetric_constraints_str(n):
  s = '# Strongly symmetric constraints. \n\n'
  for i in range(n):
    for j in range(n):
      s += 'sumgeq(' + ellell([[i,j],[n - 1 - i, n - 1 - j]]) + ', ' + str(n - 1) + ')\n'
      s += 'sumleq(' + ellell([[i,j],[n - 1 - i, n - 1 - j]]) + ', ' + str(n - 1) + ')\n'
    s += '\n'
  return s

def orthogonality_constraints_str(n):
  """Returns a string containing the orthogonality constraints for a square
  of size n."""
  F = [[(i,j), (j,i)] for i in range(n) for j in range(n)]
  s = '# Orthogonality constraints. \n\n'
  s += "".join([vecneq(p, q) + '\n' for p in F for q in F if p > q])
  return s + '\n'

def psssodls_string(n):
  """Returns a string which is the entire Minion 3 format constraint program
  for PSSSODLS(n)."""
  s = begin(n)
  s += latin_constraints_str(n)
  s += pandiagonality_constraints_str(n)
  s += strongly_symmetric_constraints_str(n)
  s += orthogonality_constraints_str(n)
  s += end()
  return s

print psssodls_string(int(sys.argv[1]))

