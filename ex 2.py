#ex 2
#Daria Polovneva
#08.09.2023
new_vanew_var = rows = 5
n = 0
for i in range(rows, 0, -1):
    n += 1
    for j in range(1, i +1):
        print(n, end = " ")
    print(" ")