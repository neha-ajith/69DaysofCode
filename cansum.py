def canSum(targetSum,numbers,memo={}):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    if targetSum in memo:
        return memo[targetSum]
    for n in numbers:
        rem = targetSum - n
        if(canSum(rem,numbers,memo) is True):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(5,[2,3]))
print(canSum(300,[8,5]))