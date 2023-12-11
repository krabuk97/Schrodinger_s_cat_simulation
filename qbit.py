import numpy as np
from qutip import basis, mesolve, ket2dm

def run_quantum_simulation():
    omega = 5.0

    H = omega * basis(2, 0) * basis(2, 0).dag() / 2 + omega * basis(2, 1) * basis(2, 1).dag() / 2

    psi0 = basis(2, 0) if np.random.rand() > 0.5 else basis(2, 1)

    times = np.linspace(0, 10, 100)

    result = mesolve(H, psi0, times, [], [basis(2, 0) * basis(2, 0).dag(), basis(2, 1) * basis(2, 1).dag()])

    return result.expect[0], result.expect[1], times


