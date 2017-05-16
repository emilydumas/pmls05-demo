'''Demonstrate computing length and dlength of a curve from matrix representations'''

import numpy as np

# Next import has output side effect; prints a 2x2 matrix
from representation import representation

# ---- BEGIN code from presentation slide ----

eps = 0.0001
rho0 = representation( {'a': np.array( [[0,1],[1,1]] )} )
rho1 = representation( {'a': np.array( [[0,1],[1+eps,1]] )} )

L0 = 2.0*np.arccosh(0.5*np.trace(rho0('aaaaa')))
L1 = 2.0*np.arccosh(0.5*np.trace(rho1('aaaaa')))

dL = (L1 - L0) / eps
print(dL)

# ---- END code from presentation slide ----

# Correct output is 2.77339786944
