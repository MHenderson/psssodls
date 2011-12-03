#!/usr/bin/env python

import sys

def ell(p):
  """This function takes a pair p = [p[0], p[1]] and returns the string
  'l[p[0],p[1]]'."""
  return 'l[' + str(p[0]) + ',' + str(p[1]) + ']'

def alldiff(v):
  """Returns a string representing an all_different constraint over the
  variables in the vector v."""
  return 'alldiff(' + v + ')'

def vecneq(p, q):
  """Returns a string representing an vectorised inequality constraint between
  the two vectors p and q."""
  return 'watchvecneq([' + ell(p[0]) + ',' + ell(p[1]) + '],[' +  ell(q[0]) + ',' + ell(q[1]) + '])'

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
  for i in range(n):
    s += alldiff(ell([i,'_'])) + '\n'
    s += alldiff(ell(['_',i])) + '\n'
  return s + '\n'

def orthogonality_constraints_str(n):
  """Returns a string containing the orthogonality constraints for a square
  of size n."""
  F = [[(i,j), (j,i)] for i in range(n) for j in range(n)]
  s = '# Orthogonality constraints. \n\n'
  for p in F:
    for q in F:
      if p > q:
        s += vecneq(p, q) + '\n'
  return s + '\n'

def psssodls_string(n):
  """Returns a string which is the entire Minion 3 format constraint program
  for PSSSODLS(n)."""
  s = begin(n)
  s += latin_constraints_str(n)
  s += orthogonality_constraints_str(n)
  s += end()
  return s

print psssodls_string(int(sys.argv[1]))

