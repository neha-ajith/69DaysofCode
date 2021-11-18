def bestSum(targetSum,numbers):
    table = [None] * (targetSum+1)
    table[0] = []
    for i in range(targetSum+1):
        if table[i] is not None:
            for n in numbers:
                try:
                    temp = table[i][:]
                    temp.append(n)
                    if table[i+n] is None or len(temp) < len(table[i+n]):
                        table[i+n] = temp[:]
                except:
                    pass
    return table[targetSum]

print(bestSum(7,[2,3,7,4]))
print(bestSum(7,[5,3,6]))
print(bestSum(100,[2,3,25]))