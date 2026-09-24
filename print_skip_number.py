total_skip_number = 1
skip_number = 0

for i in range(1, 100):
    if skip_number > 0:
        print(i)
        skip_number -= 1
    else:
        skip_number = total_skip_number
        total_skip_number += 1

