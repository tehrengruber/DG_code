import numpy as np
import sys

if len(sys.argv) == 6:
    _, nx, nz, r, runge_kutta, backend = sys.argv
    nx = int(nx)
    nz = int(nz)
    r = int(r)
    runge_kutta = int(runge_kutta)
    if backend == 'cpu':
        backend ="gt:cpu_ifirst" 
else:
    # === BACKENDS ===
    # backend = "numpy"
    # backend ="gt:cpu_ifirst" 
    # backend ="gt:cpu_kfirst" 
    # backend = "dace:cpu"
    backend = "dace:gpu"
    # backend = "cuda"

    # === ORDER ===
    # spatial rank
    r = 3
    # runge-kutta
    runge_kutta = 4
    
    nx = 100
    nz = 40

n_qp_1D = r+1
dim=(r+1)**2
n_qp = n_qp_1D**2


dtype = np.float64
# dtypes
dtype_modal2qp_matrix = (dtype, (n_qp, dim))
dtype_modal2bd_matrix = (dtype, (n_qp_1D, dim))

dtype_qp_vec = (dtype, (n_qp,))
dtype_bd_vec = (dtype, (n_qp_1D,))
dtype_modal_vec = (dtype, (dim,))

if backend == 'numpy':
    backend_opts = {
        "rebuild": False,
    }
else:
    backend_opts = {
        "rebuild": False,
        "verbose": True,
        "_validate_args": False
    }

externals = {
    "DIM": dim,
    "N_QP": n_qp,
    "N_QP_1D": n_qp_1D
}
