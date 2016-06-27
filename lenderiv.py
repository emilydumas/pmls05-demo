#!/usr/bin/python
######################################################################
## Filename:      lenderiv.py
## Description:   Compute derivatives of lengths of curves in a
##                representation of F_4 using a finite difference
## Author:        David Dumas <david@dumas.io>
## Modified at:   Mon Jun 27 11:01:25 2016
##                
## Copyright (C) 2012, 2016 David Dumas
##                
## This program is free software distributed under the GNU General
## Public License (http://www.gnu.org/licenses/gpl.txt).
######################################################################
from fgrep import *
from numpy import *
from cmath import acosh
from readcocycles import readcocycles
from zopen import zopen

DERIVEPS = 1.4901161193847656e-08

letters = 'abcdefghijklmnopqrstuvwxyz'

def hyplen(tr):
    return 2.0*(acosh(0.5*tr).real)

def dloglen(tr0,tr1,eps):
    return (hyplen(tr1) - hyplen(tr0))/(eps*hyplen(tr0));

def displace(m0list,mdotlist,epsilon):
    return [ (m0*(eye(2) + epsilon*mdot)) for m0,mdot in zip(m0list,mdotlist) ]

def wrapmatrices(mlist):
    return dict( ( (letters[i],m) for i,m in enumerate(mlist) ) )

def main():
    import argparse
    import sys
    from datetime import datetime

    parser = argparse.ArgumentParser(description='Compute d(log(length)) for free group representation cocycles.')
    parser.add_argument('cocycle_file',help='File with representation and basis of cocycles')
    parser.add_argument('word_file',nargs='?',help='File of free group words; default is stdin')
    parser.add_argument('-o','--output',help='output filename; default is stdout')

    args = parser.parse_args()
    
    with open(args.cocycle_file,'r') as infile:
        rdata = readcocycles(infile)

    if not args.word_file:
        wordfile = sys.stdin
        args.word_file = 'STDIN'
    else:
        wordfile = zopen(args.word_file,'r')

    if not args.output:
        outfile = sys.stdout
    else:
        outfile = zopen(args.output,'w')

    fg0 = FreeGroup(wrapmatrices(rdata['representation']))
    fg1list = [ FreeGroup(wrapmatrices(displace(rdata['representation'],x,DERIVEPS))) for x in rdata['cocycles'] ]

    # header
    outfile.write('# lenderiv.py output %s\n' % datetime.now())
    outfile.write('# cocycle_file = %s\n' % args.cocycle_file)
    outfile.write('# word_file = %s\n' % args.word_file)
    outfile.write('# columns are "word length (dlog(len(w))/du_i; i=1..4)"\n')

    nprocessed = 0
    for w in wordfile:
        if (not len(w)) or (w[0]=='#'):
            continue
        w = w.strip()
        tr0 = trace(fg0[w])
        logvec = [ dloglen(tr0,trace(fg1[w]),DERIVEPS) for fg1 in fg1list ]
        outfile.write('%s %.15f %.15f %.15f %.15f %.15f\n' % (w,hyplen(tr0),logvec[0],logvec[1],logvec[2],logvec[3]))
        nprocessed += 1
        if nprocessed % 1000 == 0:
            sys.stderr.write('.')
    sys.stderr.write('\n')
    outfile.close()

if __name__=='__main__':
    main()
