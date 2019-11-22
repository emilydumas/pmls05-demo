######################################################################
## Filename:      readcocycles.py
## Description:   Read and parse list of cocycles for F_4
## Modified at:   Wed Jun 29 16:18:11 2016
##                
## From the PML Visualization Project (http://dumas.io/PML/)
## by David Dumas and Francois Gueritaud
##
## This program is free software distributed under the GNU General
## Public License (http://www.gnu.org/licenses/gpl.txt).
######################################################################

# Expects a format like the one generated in pentagon-calculations.nb
# i.e
#
# representation
# <list of matrix entries of representation, one per line>
# cocycles
# <list of matrix entries of cocycles, one per line>

from numpy import *

def numlist_to_dict(f):
    d = {}
    curkey = 'unnamed'
    for line in f:
        line = line.strip()
        if len(line)==0:
            continue
        if line[0]=='#':
            continue
        try:
            n = float(line)
            if not (curkey in d):
                d[curkey] = []
            d[curkey].append(float(line))
        except ValueError:
            curkey = line
    return d

def get2by2s(L):
    mlist = []
    while len(L) > 0:
        mlist.append( matrix( [[ L[0],L[1] ], [ L[2],L[3] ]] ) )
        L = L[4:]
    return mlist
    

def readcocycles(f):
    d = numlist_to_dict(f)
    mrep = get2by2s(d['representation'])
    rank = len(mrep)
    mco = get2by2s(d['cocycles'])
    mcol = []
    while len(mco) > 0:
        mcol.append( mco[:rank] )
        mco = mco[rank:]
    return { 'representation': mrep, 'cocycles': mcol }

def main():
    import sys
    d = readcocycles(sys.stdin)
    print('Representation of rank ',len(d['representation']))
    for j,g in enumerate(d['representation']):
        print('g%d = ' % (j+1), g)
    print('Read %d cocycles' % len(d['cocycles']))
    for i,c in enumerate(d['cocycles']):
        print('Cocycle ',i+1,':')
        for j,g in enumerate(d['cocycles'][i]):
            print('g%ddot = ' % (j+1), g)

if __name__=='__main__':
    main()
