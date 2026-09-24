#find the lowest number :
# Welcome to your Python project!
List1 = [1,2,3]
List2 = [4,-5,6]
List3 =[10,11,-12]



def find_with_lowest(List1,List2,List3):
    combine = List1 +List2 +List3
    lowest = 0
    for i in combine :
        if i < lowest :
            lowest = i
    print(lowest)
    if lowest in List1:
        print(List1)
    elif lowest in List2:
        print(List2)
    elif lowest in List3:
        print(List3)



find_with_lowest(List1,List2,List3)`