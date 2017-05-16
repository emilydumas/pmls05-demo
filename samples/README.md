# Code samples from PML project talks

## Requirements

* [Python 2.7 or 3.5+](http://python.org/)
* [Numpy](http://www.numpy.org/) (tested with v1.11.0)

## Contents

* [```cartesian.py```](cartesian.py) : Naive cartesian product word
  generator.

* [```generator.py```](generator.py) : Twist-based simple curve
  generator.

* [```representation.py```](representation.py) : Compute the 2x2
  matrix associated to a curve.

* [```length.py```](length.py) : Compute the hyperbolic length
  of a curve and a tiling, and dlength associated to a curve and a
  deformation of the tiling.

## Simplifications

The following simplifications have been applied to this "tutorial" code (in
comparison to the full rendering demo found in this same repository):

* Words are represented as strings.  The full demo uses tuples of
  integers (with ```1 = a```, ```2 = b```, ```-1 = A```, ```-2 = B```
  etc.) as this makes certain filtering steps simpler.
  
* No word reduction is applied.  Whenever a letter appears adjacent to
  its inverse (e.g. ```aA``` or ```Cc```) this pair can be removed
  without changing the curve, however this _reduction_ step is skipped
  in these code samples.
  
* Conjugacy class and orientation duplicates are retained.  The curves
  ```abc```, ```bca```, and ```cab``` and their inverses all represent
  the same curve (differing only in orientation and the choice of a
  starting point).  This applies more generally to cyclic permutations
  of a word and their inverses.  As these all have the same dlength
  vector, only one representative from each such equivalence class
  should be retained; however, this is ignored in these code samples.
  
* Reduction to F_4 is skipped.  The generator ```e``` is redundant
  because it represents the same curve as ```DCBA```.  This
  substitution should be applied to all of the 5-generator words
  before applying the reduction and conjugacy class filtering steps
  described above.

## Comments, questions, bug reports

* David Dumas <david@dumas.io>
