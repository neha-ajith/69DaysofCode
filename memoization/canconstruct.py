def canConstruct(target,words,memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for w in words:
        try:
            if target.index(w) == 0:
                prefix = target[len(w):]
                if canConstruct(prefix,words) is True:
                    memo[target] = True
                    return True
        except:
            pass
    memo[target] = False       
    return False

print(canConstruct('abcdef',['ab','abc','abcd','def','cd']))
print(canConstruct('skateboard',['s','k','t','ate','bo','boar']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))

# try:
# print("Hire the top freelancers".index("hire"))
# except ValueError:
#     print("Does not exist")