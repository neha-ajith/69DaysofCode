def howSum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for n in numbers:
        rem = targetSum - n
        res = howSum(rem,numbers,memo)
        if res is not None:
            memo[targetSum] = res.append(n)
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(30,[2,3]))
print(howSum(300,[2,3]))