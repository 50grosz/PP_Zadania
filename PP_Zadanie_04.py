num = int(input("Give me a number"))
my_num = []
x = range (1, num + 1)

for i in x :
    if num % i == 0:
        my_num.append(i)
print(my_num)
