from scipy.stats import norm
import numpy as np

def delta(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return norm.cdf(d1) if option_type == 'call' else norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    
    if T <= 0: return 0.0 # Vega is zero at expiration

    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    vega_val = S * np.sqrt(T) * n(d1)
    return vega_val / 100 # Often presented per 1% change in volatility

def theta(S, K, T, r, sigma, option_type='call'):

    if T <= 0: return 0.0 # Theta is zero at expiration

    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        theta_val = (- (S * n(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * N(d2))
    elif option_type == 'put':
        theta_val = (- (S * n(d1) * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * N(-d2))
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return theta_val / 365 # Often presented as daily decay

def rho(S, K, T, r, sigma, option_type='call'):
   
    if T <= 0: return 0.0 # Rho is zero at expiration

    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        rho_val = K * T * np.exp(-r * T) * N(d2)
    elif option_type == 'put':
        rho_val = -K * T * np.exp(-r * T) * N(-d2)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
        
    return rho_val / 100 # Often presented per 1% change in interest rate
