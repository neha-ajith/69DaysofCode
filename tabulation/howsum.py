def howSum(targetSum,numbers):
    table = [None for i in range(targetSum+2)]
    table[0] = []
    for i in range(targetSum+1):
        if table[i] is not None:
            for n in numbers:
                try:
                    table[i+n] = table[i][:]
                    table[i+n].append(n)
                    # print(table[i])
                    # print(table[i+n])
                except:
                    pass
    return table[targetSum]

print(howSum(7,[2,3]))
print(howSum(7,[5,3,6]))