def countConstruct(target,words,memo={}):
    totalCount = 0
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    for w in words:
        try:
            if target.index(w) == 0:
                prefix = target[len(w):]
                totalCount += countConstruct(prefix,words,memo)
        except:
            pass
    memo[target] = totalCount
    return totalCount

print(countConstruct('abcdef',['ab','abc','abcd','def','cd']))
print(countConstruct('skateboard',['s','k','t','ate','bo','boar']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))

