import numpy as np 
import math 

def rouwenhorst(
    N : int, 
    ρ : float,
    σ : float,
    μ : float = 0.0):
    """
    #=#############################################################################
    # SUBROUTINE discretize_AR
    #
    # Discretizes an AR(1) process of the form z_j = \rho*z_{j-1} + eps using
    #     the Rouwenhorst method.
    #
    # REFERENCE: Kopecky, K.A., Suen, R.M.H., Finite state Markov-chain 
    #            approximations to highly persistent processes, Review of Economic
    #            Dynamics, Vol. 13, No. 3, 2010, 701-714.
    =##############################################################################
    """

    σ_y = σ / math.sqrt(1-ρ^2)
    p  = (1+ρ)/2
    ψ = math.sqrt(N-1) * σ_y
    m = μ / (1 - ρ)



def  _rouwenhorst(p : float, 
                  q : float, 
                  m : float, 
                  Δ : float, 
                  n : int)

    if n == 2:
        return np.array([m-Δ, m+Δ]),  np.array([[p 1-p], [1-q q]])
    else :
        _, θ_nm1 = _rouwenhorst(p, q, m, Δ, n-1)
        