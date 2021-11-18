def bestSum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortest = None
    for n in numbers:
        rem = targetSum - n 
        res = bestSum(rem,numbers,memo)
        if res is not None:
            res.append(n)
            if shortest is None or len(res) < len(shortest):
                shortest = res
    memo[targetSum] = shortest
    return memo[targetSum]

print(bestSum(7,[3,3]))
print(bestSum(300,[2,3,5]))