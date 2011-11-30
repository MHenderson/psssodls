#!/usr/bin/env python

# Created on 30 November 2011. Last updated 30 November 2011.

def f(n):
  return [[(i,j), (j,i)] for i in range(n) for j in range(n)]

def ell(p):
  return 'l[' + str(p[0]) + ',' + str(p[1]) + ']'

def vecneq(p, q):
  return 'watchvecneq([' + ell(p[0]) + ',' + ell(p[1]) + '],[' +  ell(q[0]) + ',' + ell(q[1]) + '])'

for p in f(8):
  for q in f(8):
      if p > q:
        print vecneq(p, q)
