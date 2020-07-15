prime_list = []
for num in range(2,101):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        prime_list.append(num)
print(prime_list)
