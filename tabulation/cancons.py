# solve the same in js.

def canConstruct(target,words):
    table = [False] * (len(target)+1)
    table[0] = True
    for i in range(len(target)+1):
        if table[i] is True:
            for w in words:
                # print(target)
                print(target[i:len(w)])
                # print(w)
                if target[i:len(w)] == w:
                    # try:
                    table[i+len(w)] = True
                        # print(target[i:len(w)])
                        # print(w)
                    # except:
                    #     pass
    return table
    # [len(target)]

print(canConstruct('abcdef',['ab','abc','abcd','def','cd']))
# print(canConstruct('skateboard',['s','k','t','ate','bo','boar']))
# print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeee']))

