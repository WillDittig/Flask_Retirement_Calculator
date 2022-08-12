def compound_interest(P,R,N,T):
    Amount = P *(pow((1+(R/N)), N*T))
    Interest = Amount - P 