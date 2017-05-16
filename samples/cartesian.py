'''Demonstrate iteration over cartesian product (a naive curve generator)'''

def is_simple_curve(w):
    # We could put an actual test for simple curves here.  However,
    # the fraction of simple words approaches zero as the length goes
    # to infinity.

    # For this code sample we simply return True for all inputs.
    return True


# ---- BEGIN code from presentation slide ----

from itertools import product

N = 5

for w in product('abcdeABCDE',repeat=N):
    if is_simple_curve(w):
        print(''.join(w))

# ---- END code from presentation slide ----
