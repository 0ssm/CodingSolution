n = int(input("enter a number: "))
is_prime = True
if n == 1 or n == 0:
    print("prime number start from 2")
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print("its a prime number: ")
    else:
        print("its not a prime number")