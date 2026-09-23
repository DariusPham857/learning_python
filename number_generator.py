#  evens, odds, multiples_of_five
# even(200)
# 2, 4, ..... 200

def even(number):
	for i in range ( 1 ,number):
		if (i%2 == 0):
			print (i)
even(20)

def odds(number):
	for i in range ( 1,number):
		if ( i%2 != 0):
			print (i)
odds (20)


def multiples_of_five(number):
	for i in range (1,number):
		if (i%5 ==0):
			print (i)

multiples_of_five(20)
