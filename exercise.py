students = ["Ninh", "Duc", "Khoa", "Kiet", "Sushil", "Salekin", "Khoi"]


## all the students in odd index will learn Math
## all the students in even index will learn English
##
##  Hello Ninh! You will learn English today
##  Hello Duc! You will learn Math today
## ..
## ..

def odd_and_even_student(students):
    for i in range (0,len(students)):
        if i%2== 0 :
            print (f"Hello {students[i]}! You will learn English today ")
        else :
            print (f"Hello {students[i]}! You will learn Math today")

# odd_and_even_student(students)


## return 2 lists
## math_students = [ odds ]
## en_students = [ evens ]

def divide_in_groups(students):
    math_students = []
    en_students = []

    for i in range(0,len(students)):
        if i%2 == 0:
            en_students.append(students[i])
        else:
            math_students.append(students[i])

    return math_students, en_students

m , e = divide_in_groups(students)

print(m)
print(e)
