number_print=[]
skip_next =0
for i in range(1,100):
    if (skip_next ==0):
        number_print.append(i)
        skip_next = len(number_print)
    else:
        skip_next -=1


print(number_print)

for i in range(len(number_print)-1, -1, -1):
    print(number_print[i])
n