# Program to check if a number is prime or not

num = int(input("Enter a number to be checked if it is prime or not : "))

# prime numbers are greater than 1
if num > 1:
    
    for i in range(2, num):
        
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number.")
# if num is less than 1
# it is not prime as well
else:
    print(num, "is not a prime number.")
