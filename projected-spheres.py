#!/usr/bin/python
######################################################################
## Filename:      projected-spheres.py
## Description:   Rotate and stereographically project, generate
##                POV-Ray sphere primitives
## Author:        David Dumas <david@dumas.io>
## Modified at:   Mon Jun 27 11:39:33 2016
##                
## Copyright (C) 2012, 2016 David Dumas
##                
## This program is free software distributed under the GNU General
## Public License (http://www.gnu.org/licenses/gpl.txt).
######################################################################

# Expected input is in the form of "lenderiv.py" output, lines like
# aDCBdbcd 14.66 -0.57 0.00 -0.87 -1.02
# <word> <curlen> <dlen/dx1> <dlen/dx2> ...

import sys
from numpy import *
from numpy import linalg

# Optional rotation angle
# Linearly increasing this gives the animation at:
#   http://youtu.be/F2se_r0sMMM
THETA=0.1

def rot(theta):
    return matrix( [[ cos(theta), -sin(theta), 0, 0],
                    [ sin(theta), cos(theta), 0, 0],
                    [ 0, 0, 1, 0],
                    [ 0, 0, 0, 1]] )

def normalize(v):
    w = (1.0 / linalg.norm(v))*v
    return w

def stereo(v):
    return array([ v[0], v[2], v[3] ]) / (1.0 - v[1])

def transform(T,v):
    return array(transpose((T * transpose(matrix(v)))))[0]

def project(v,theta):
    return stereo(transform(rot(theta),normalize(v)))

nprocessed = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line[0] == '#':
        continue
    fields = line.split()
    w = fields[0]
    L = float(fields[1])
    p = array([float(x) for x in fields[2:]])
    r = 0.6 / pow(L,1.2)
    C = project(p,THETA)
    print 'sphere { <%f,%f,%f>, %f }' % (C[0],C[1],C[2],r)
    nprocessed += 1
    if nprocessed % 1000 == 0:
	sys.stderr.write('.')
sys.stderr.write('\n')

