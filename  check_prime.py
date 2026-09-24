def check_prime(number):
    if number == 1:
        return "not prime"

    limit= number//2+1

    for i in range (2,limit):
        if number % i ==0 :
            return(f"{number}:  not prime")
    return ("prime")

for i in range(1,100):
    if check_prime(i) =="prime":
        print(i)
