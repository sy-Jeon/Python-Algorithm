def fib_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        fib = fib_naive(n-1) + fib_naive(n-2)
        return fib
    
fib_naive(5)
