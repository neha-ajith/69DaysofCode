def allConstruct(target,words,memo={}):
    result = []
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    for w in words:
        try:
            if(target.index(w) == 0):
                suffix = target[len(w):]
                returnList = allConstruct(suffix,words,memo)
                targetWays = addElement(returnList,w)
                addList(result,targetWays)
        except:
            pass
    memo[target] = result
    return result 

def addList(arr1,arr2):
    for b in arr2:
        arr1.append(b)
        return arr1

def addElement(arr1,val):
    for a in arr1:
        a.append(val)
    return arr1

# ar = [[1],[2,2]]
# print(addElement(ar,[[]]))
print(allConstruct('abcdef',['ab','abc','abcd','def','cd','c','d']))
print(allConstruct('skateboard',['s','k','t','ate','bo','boar']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))
