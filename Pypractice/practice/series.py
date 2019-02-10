import os
def prime_numbers(limit):
    print("\nprime numbers : ")
    primes = [x for x in range(2, limit) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
    print(primes)
def armstrong_numbers(limit):
    print("\narmstrong numbers : ")
    armstrong = [x for x in range(limit) if sum(list(map(lambda y: y ** len(str(x)), list(map(int, str(x)))))) == x]
    print(armstrong)
p = 0
while p != 4:
    print("\nPress 1 for list of prime numbers\nPress 2 for list of armstrong numbers\nPress 3 to clear screen\nPress 4 to exit")
    p = int(input())
    if p is 1:
        lim = int(input("Enter range limit : "))
        prime_numbers(lim)
    elif p is 2:
        lim = int(input("Enter range limit : "))
        armstrong_numbers(lim)
    elif p is 3:
        os.system("cls")
    else:
        os.system("cls")
        print("Goodbye")
        break
