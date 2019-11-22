######################################################################
## Filename:      zopen.py
## Description:   Transparently open/create a compressed file
## Modified at:   Wed Jun 29 16:17:55 2016
##                
## From the PML Visualization Project (http://dumas.io/PML/)
## by David Dumas and Francois Gueritaud
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
        f = open(fn,mode)
    return f
    
