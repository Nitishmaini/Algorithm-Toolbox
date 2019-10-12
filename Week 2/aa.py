# Uses python2
from functools import reduce
import sys
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    gcd(a,b)
    print(lcm(a, b))
