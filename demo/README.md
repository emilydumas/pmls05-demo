# PML(S_{0,5}) Rendering Demonstration

## Requirements

* [Python 2.7](http://python.org/)
* [Numpy](http://www.numpy.org/) (tested with v1.11.0)
* Posix shell environment
* [POV-Ray 3.6+](http://www.povray.org/) (only required for rendering)

## QUICK START

1. Run the script ```make-pml-image.sh```
2. View the output image ```pmls05-image.png```

The resulting image shows 19765 spheres representing simple closed
curves on the five-punctured sphere, positioned according to the
stereographic projection of Thurston's d(log(length)) embedding in the
cotangent space of Teichmueller space.

## The process

The script ```make-pml-image.sh``` performs the following steps to create
the image:

1. __Cocycles__

The file ```pent2.csv``` contains generators of a Fuchsian group
corresponding to a hyperbolic structure on the five-punctured sphere
and a collection of shearing cocycles that form a basis of the tangent
space to Teichmuller space at this point.  This is the _cocycle file_.

The Mathematica notebook "pentagon-calculations.nb" generates the
cocycle file; however, the cocycle file is included with the demo
source code so that mathematica is not required.

2. __Words__

The script ```scc.py``` generates a list of simple closed curves on the
five-punctured sphere by exploring a Cayley graph of the braid group
to a certain depth.  The result is a list of elements of the free
group F_4, comprising a _word file_.

In this demo, the word file is ```words.txt```.

3. __Covectors__

The script ```lenderiv.py`` reads a cocycle file and word file and
computes the derivative of the logarithm of hyperbolic length for each
of the simple closed curves in the direction of each shearing cocycle.
These are written to a _covector file_.

In this demo, the covector file is ```covectors.txt```.

4. __Projection and scene file__

The script ```projected-spheres.py``` converts the data in the
covector file to a set of POV-Ray sphere primitives by rotating and
stereographically projecting the covectors and then generating POV-Ray
sphere primtives with appropriate radii.  The result is the _sphere
file_, which in this demo is called ```spheres.inc```.

5. __Rendering__

Finally, [POV-Ray 3.6+](http://www.povray.org/) is called to render
the scene described in ```scene.pov```.  This scene files imports the
sphere file after setting parameters such as camera position and
lighting.


## Further exploration

To explore this demo further, you might try:

* __Scaling up the computation__: Show more curves by increasing the
  maximum depth in the braid group.  The default is ```7```; this is
  the first positional argument passed to ```scc.py``` in
  ```make-pml-image.sh```.

* __Animation: Rotating in R^3__: The scene file ```scene.pov``` is configured for
  rendering an animation of the cloud of spheres rotating about the z
  axis.  After generating the covector file, a 30-frame animation can
  be created using a command such as

      povray +Opmls05-anim-frame.png +KFI1 +KFF30 +KC render.ini
    
  The output will consist of frames named
  ```pmls05-anim-frame01.png```, ```pmls05-anim-frame02.png``` etc.

* __Animation: Rotating in R^4__: The script ```projected-spheres.py``` includes
  an angle parameter ```THETA``` which specifies a rotation in
  4-dimensional space to apply before stereographically projecting the
  covectors to R^3.  Modify this script to make ```THETA``` a
  command-line argument and render images for a sequence of values
  between 0 and 2*pi to create an animation.  This reproduces the
  animation shown at: http://youtu.be/F2se_r0sMMM

Note about animations:  A video encoder tool such as [FFmpeg](https://ffmpeg.org) can be used
to convert a sequence of frame images to a video file for convenient
playback.  A simple frontend to FFmpeg for this purpose is
[ddencode](https://github.com/daviddumas/ddencode).

## Comments, questions, bug reports

* David Dumas <david@dumas.io>
