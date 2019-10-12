# Uses python3
def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

n = int(input())
print(fib_to(n))
