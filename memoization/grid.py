def grid(m,n,memo = {}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    memo[key] = grid(m-1,n,memo) + grid(m,n-1,memo)
    return memo[key]

print(grid(2,3))
print(grid(18,18))