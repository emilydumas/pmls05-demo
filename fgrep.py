#!/usr/bin/python
######################################################################
## Filename:      fgrep.py
## Description:   Calculate with a free group matrix representation
## Author:        David Dumas <david@dumas.io>
## Modified at:   Wed Nov 28 14:25:58 2012
##                
## Copyright (C) 2012 David Dumas
##                
## This program is free software distributed under the GNU General
## Public License (http://www.gnu.org/licenses/gpl.txt).
######################################################################

from numpy import *
from numpy import linalg
import re
import string

lcase = 'abcdefghijklmnopqrstuvwxyz'
ucase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
wordre = re.compile(r'[A-Za-z]+')

class FreeGroup(dict):
    '''Matrix group class where generators are represented by lower-case letters'''
    def __init__(self,gens):
        self.n = None
        for k in gens:
            if isinstance(k,str) and len(k)==1 and k in lcase:
                self[k] = gens[k]
            else:
                raise KeyError('Bad generator key (%s), need lower-case letters.' % str(k))
            sh = gens[k].shape
            if self.n:
                if sh != (self.n,self.n):
                    raise ValueError('Bad matrix size %s; should be (%d,%d).' % (str(sh),self.n,self.n))
            else:
                self.n = sh[0]
                if sh[1] != self.n: 
                    raise ValueError('Bad matrix size %s; should be (%d,%d).' % (str(sh),self.n,self.n))
        keys = self.keys()
        ukeys = [ k.upper() for k in keys ]
        self.alphabet = string.join(keys + ukeys,'')

    def __getitem__(self, k):
        if k=='':
            return eye(self.n,dtype=complex)
        if len(k)==1:
            if k in lcase:
                return dict.__getitem__(self,k)
            elif k in ucase:
                m=dict.__getitem__(self,k.lower())
                return linalg.inv(m)
            else:
                raise KeyError('Bad key (%s), need string of characters from alphabet %s' % (k,self.alphabet))
        elif wordre.match(k):
            return self[k[:len(k)/2]] * self[k[len(k)/2:]]
        else:
            raise KeyError('Bad key (%s), need string of characters from alphabet %s' % (k,self.alphabet))

if __name__ == '__main__':
    def matstr(m):
        return str(m).replace('\n',',')
    gens = { 'a' : matrix([[1,1],[0,1]]), 'b':matrix([[1,0],[1,1]]) }
    F = FreeGroup(gens)
    words = [ 'a', 'b', 'A', 'B', 'ab', 'ba', 'aB', 'Ba', 'abBA', 'aaa', 'aabaBBA']
    print F.keys()
    for w in words:
        print '%s = %s' % (w,matstr(F[w]))

