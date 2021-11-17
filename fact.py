def fact(n,memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    memo[n] = n * fact(n-1)
    return memo[n]

print(fact(5))
print(fact(1000))