#!/bin/bash

#----------------------------------------------------------------------
# RUN THIS SCRIPT IN THE directory where the source distribution was unpacked.
#----------------------------------------------------------------------

#----------------------------------------------------------------------
echo WORD FILE
./scc.py 7 -o words.txt

#----------------------------------------------------------------------
echo COVECTOR FILE

./lenderiv.py -o covectors.txt pent2.csv words.txt

#----------------------------------------------------------------------
echo SPHERE FILE
#
# Note: Unlike the other scripts, this one acts as a pipe, reading 
# from STDIN and writing to STDOUT

./projected-spheres.py < covectors.txt > spheres.inc

#----------------------------------------------------------------------
# IMAGE
#
# Note: "render.ini" specifies that the scene is in "scene.pov"

povray +Opmls05-image.png render.ini 
