def gridTraveler(m,n):
    table = [[0 for i in range(n+1)] for j in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            try:
                current = table[i][j]
                if(i+1 <= m):
                    table[i+1][j]+=current
                if(j+1 <= n):
                    table[i][j+1]+=current
            except:
                pass
    return table[m][n]

print(gridTraveler(3,3))
print(gridTraveler(18,18))