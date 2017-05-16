'''Demonstrate computing 2x2 matrix representation from strings'''

# ---- BEGIN code from presentation slide ----

import numpy as np

def representation(gen_matrices):
    def _rho(x):
        if len(x) == 0:
            # identity matrix
            return np.eye(2)
        elif len(x) == 1:
            # generator matrix
            return gen_matrices[x]
        else:
            N = len(x)
            return np.dot(_rho(x[:N//2]),_rho(x[N//2:]))
    return _rho

rho = representation( {'a': np.array( [[0,1],[1,1]] )} ) # etc

print(rho('aaaaa'))  # -> [[3 5], [5 8]]

# ---- END code from presentation slide ----
