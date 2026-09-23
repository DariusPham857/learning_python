def odds(n):
    odds=[]
    i=1
    while (i <n):
        if i % 2 !=0:
            odds.append(i)
        i+=1
    return odds
res = odds(50)
print(res)

