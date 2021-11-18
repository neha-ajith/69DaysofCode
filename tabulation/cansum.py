def canSum(targetSum,numbers):
    table = [False]*(targetSum+1)
    table[0] = True 
    for i in range(targetSum+1):
        for n in numbers:
            try:
                if table[i] is True:
                    table[i+n] = True
            except:
                pass
    return table[targetSum]

print(canSum(7,[5,3,4]))
print(canSum(7,[5,3,6]))