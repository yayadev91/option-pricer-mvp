import numpy as np

def compute_d1(S, K, T, r, sigma):
    return (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))

def compute_d2(d1, sigma, T):
    return d1 - sigma * np.sqrt(T)