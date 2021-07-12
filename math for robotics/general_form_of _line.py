from fractions import Fraction

def lineForm_S2G(m,b):
    A, B, C = -m , 1 ,-b
    if A < 0:
        A, B, C = -A, -B, -C
    denA = Fraction(A).limit_denominator(1000).as_integer_ratio()[1]
    denC = Fraction(C).limit_denominator(1000).as_integer_ratio()[1]

    gcd = np.gcd(denA, denC)
    lcm = denC * denA/gcd

    A = A * lcm
    B = B * lcm
    C = C * lcm
    return A,B,C