#!/usr/bin/env python3
######################################################################
## Filename:      scc.py
## Description:   Generate list of simple closed curves on S_{0,5}
## Modified at:   Wed Jun 29 16:18:35 2016
##                
## From the PML Visualization Project (http://dumas.io/PML/)
## by David Dumas and Francois Gueritaud
##                
## This program is free software distributed under the GNU General
## Public License (http://www.gnu.org/licenses/gpl.txt).
######################################################################

'Find words representing simple close curves on the punctured sphere'

#----------------------------------------------------------------------
# FREE GROUP ROUTINES
# 
# We represent an element of the free group as a tuple of nonzero
# integers, each of which represents a generator (if positive) or its
# inverse (if negative).  Here we implement functions for reducing,
# cyclically reducing, and finding a canonical representative of the
# conjugacy class of any given word.
#----------------------------------------------------------------------

_alpha = 'abcdefghijklmnopqrstuvwxyz'
_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def _makeletter(k):
    global _alpha,_ALPHA
    if k==0:
        raise ValueError('Generator index must be positive.')
    if k>0:
        return _alpha[k-1]
    else:
        return _ALPHA[-k-1]

def _makeint(c):
    global _alpha,_ALPHA
    i=_alpha.find(c)
    if i>=0:
        return i+1
    i=_ALPHA.find(c)
    if i>=0:
        return -(i+1)
    else:
        raise ValueError('Generator letter not found.')

def prettyprint(w):
    return ''.join( (_makeletter(k) for k in w) )
    
def fromstring(s):
    return tuple( (_makeint(c) for c in s) )

def inverse(w):
    return tuple( -x for x in w[::-1] )

def reduce_word(w0):
    w = ()
    for x in w0:
        if len(w)>0 and (w[-1] == -x):
            w = w[:-1]
        else:
            w = w + (x,)
    return w

def cyc_reduce_word(w0):
    w = reduce_word(w0)
    while (len(w)>1) and (w[0] == -w[-1]):
        w = w[1:-1]
    return w

def rotate(w,i):
    if i==0:
        return w
    i = i % len(w)
    return w[i:] + w[:i]

def compare(i,j):
    return (i>j)-(j<i)

def mycmp(i,j):
    if i>0 and j>0:
        return compare(i,j)
    if i>0 and j<0:
        return -1
    if i<0 and j>0:
        return 1
    return compare(-i,-j)

def mylexcmp(x,y):
    for i in range(min(len(x),len(y))):
        c = mycmp(x[i],y[i])
        if c != 0:
            return c
    return compare(len(x),len(y))

def lexmin(w0):
    if len(w0)<2:
        return w0
    w = w0
    for i in range(1,len(w0)):
        wnew = rotate(w0,i)
        if mylexcmp(wnew,w) < 0:
            w = wnew
    w0 = inverse(w0)
    for i in range(len(w0)):
        wnew = rotate(w0,i)
        if mylexcmp(wnew,w) < 0:
            w = wnew
    return w

def conj_class_rep(w):
    return lexmin(cyc_reduce_word(w))

def wrapper(x):
    try:
        return tuple(x)
    except TypeError:
        return tuple([x])

#----------------------------------------------------------------------
# ENDOMORPHISM
#
# This class represents an endomorphism of the free group, represented
# as a list of images of the generators.  This is essentially a
# function factory implemented as a callable class which applies the
# endomorphism to a given word.
#----------------------------------------------------------------------

class endomorphism(object):
    __slots__ = ['images']
    def __init__(self,*args):
        self.images = [ wrapper(x) for x in args ]
    def __call__(self,x):
        t = ()
        for i in x:
            if (i>0):
                t = t + self.images[i-1]
            else:
                t = t + inverse(self.images[-i-1])
        return t

def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Generate list of simple closed curves on the 5-punctured sphere.')
    parser.add_argument('depth',type=int)
    parser.add_argument('-o','--output',help='output filename; default is stdout')

    args = parser.parse_args()

    # NOTE: We work in F_5 even though we ultimately want words in
    # pi_1(S_05) = F_4 The reason is that we also want a list of
    # curves that is invariant under the natural order-5 rotation
    # symmetry of the sphere (which acts on the 5-element redundant
    # generating set as a 5-cycle)

    # AFTER generating the list we project down to F_4.


    # Initialize the pool with a few simple closed curves
    pool = set()
    work = set( [conj_class_rep(x) for x in [ (1,2), (2,3), (3,4), (4,5), (5,1) ]] )

    # These automorphisms are elements of the braid group.  We apply
    # them to the curves known so far to generate new ones.
    gens = [ endomorphism((1,2,-1),1,3,4,5),  # 12 twist
             endomorphism(2,(-2,1,2),3,4,5),  # 12 inverse
             endomorphism(1,(2,3,-2),2,4,5),  # 23 twist
             endomorphism(1,3,(-3,2,3),4,5),  # 23 inverse
             endomorphism(1,2,(3,4,-3),3,5),  # 34 twist
             endomorphism(1,2,4,(-4,3,4),5),  # 34 inverse
             endomorphism(1,2,3,(4,5,-4),4),  # 45 twist
             endomorphism(1,2,3,5,(-5,4,5)),  # 45 inverse
             endomorphism(5,2,3,4,(5,1,-5)),  # 51 twist
             endomorphism((-1,5,1),2,3,4,1) ] # 51 inverse

    # Generate words in F_5
    for n in range(0,args.depth):
        # Apply generators
        new_work = set( conj_class_rep(g(w)) for w in work for g in gens )
        # Remove duplicates (those curves which were known at last step)
        new_work.difference_update(work)

        pool.update(work)
        print('# F_5: generation %d: %d in pool' % (n,len(pool)))
        work = new_work

    pool.update(work)
    print('# F_5: generation %d: %d in pool' % (args.depth,len(pool)))

    # Substitute down to F_4
    projector = endomorphism( 1, 2, 3, 4, (-4,-3,-2,-1) )
    pool4 = set( conj_class_rep(projector(w)) for w in pool )

    print('# F_4: %d words remain' % (len(pool4)))

    # Write output to a file
    if args.output:
        outfile = open(args.output,'wt')
    else:
        outfile = sys.stdout
    for w in pool4:
        outfile.write('%s\n' % prettyprint(w))
    outfile.close()

if __name__ == '__main__':
    main()
