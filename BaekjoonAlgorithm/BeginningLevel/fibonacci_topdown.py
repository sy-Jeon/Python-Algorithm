fib_array = [0, 1]

def fib_recur_dp(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_array.append(fib)
        return fib

fib_recur_dp(4)
