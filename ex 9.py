#ex 9
#Daria Polovneva
#08.09.2023
n = 1
m = 2
y = 2
for i in range(2, 6):
    for j in range(n, m):
        y -= 1
        print(y, end = " ")
    print(" ")
    n = m
    m += i
    y = m