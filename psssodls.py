#!/usr/bin/env python

import sys

def ell(p):
  return 'l[' + str(p[0]) + ',' + str(p[1]) + ']'

def orthogonality_constraints_str(n):
  def f(n):
    return [[(i,j), (j,i)] for i in range(n) for j in range(n)]
  def vecneq(p, q):
    return 'watchvecneq([' + ell(p[0]) + ',' + ell(p[1]) + '],[' +  ell(q[0]) + ',' + ell(q[1]) + '])'
  s = ''
  for p in f(n):
    for q in f(n):
      if p > q:
        s += vecneq(p, q) + '\n'
  return s

def psssodls_string(n):
  s = ''
  s += orthogonality_constraints_str(n)
  return s

print psssodls_string(int(sys.argv[1]))

