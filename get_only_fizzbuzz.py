

def OnlyFizzBuzz(start,end):
    Only_FizzBuzz=[]
    for i in range (31,80):
        if i%15 ==0 :
            Only_FizzBuzz.append([i])
    return Only_FizzBuzz
results = OnlyFizzBuzz(31,80)
print(results)



