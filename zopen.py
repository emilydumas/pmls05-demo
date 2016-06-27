######################################################################
## Filename:      zopen.py
## Description:   Transparently open/create a compressed file
## Author:        David Dumas <david@dumas.io>
## Modified at:   Wed Nov 28 14:27:29 2012
##                
## Copyright (C) 2012 David Dumas
##                
## This program is free software distributed under the GNU General
## Public License (http://www.gnu.org/licenses/gpl.txt).
######################################################################

def zopen(fn,mode):
    if fn.endswith('.bz2'):
        import bz2
        f = bz2.BZ2File(fn,mode)
    elif fn.endswith('.gz'):
        import gzip
        f = gzip.GzipFile(fn,mode)
    else:
        f = file(fn,mode)
    return f
    
