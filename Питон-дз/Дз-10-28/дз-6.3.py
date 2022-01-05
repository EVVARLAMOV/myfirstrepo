def bank(a, years):
    b = 0
    while years != 0:
        a *= 1.1
        years -= 1
    return(a)
