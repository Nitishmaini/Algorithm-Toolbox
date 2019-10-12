# Uses python3
import sys

def lcm_naive(a, b):
    if(a>b):
        g = a
    else:
        g = b
    while(True):  
       if((g % a == 0) and (g % b == 0)):  
           lcm = g  
           break  
       g += 1  
    return lcm  
    
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
