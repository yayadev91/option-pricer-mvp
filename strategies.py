def covered_call(S0, K, premium):
    def payoff(S_T):
        return max(S_T - S0, 0) - max(S_T - K, 0) + premium
    return payoff