a=[1,5,7]
b=[4,3,2]
c=[8,-1,3]

def sum_list(Lit):
    total_sum =0
    for i in Lit:
        total_sum += i
    return total_sum
sum_list_1 = sum_list(a)
sum_list_2 = sum_list(b)
sum_list_3 = sum_list(c)

if sum_list_1 > sum_list_2 and sum_list_1 > sum_list_3:
    print(a)
elif sum_list_2 > sum_list_1 and sum_list_2 > sum_list_3 :
    print(b)
elif sum_list_3 > sum_list_1 and sum_list_3 > sum_list_1 :
    print(c)  
