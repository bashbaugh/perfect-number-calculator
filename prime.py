f = open("resultsPrime.txt", "a")
currnum = 3;
primes = [2]

def calc():
    global currnum, primes
    for prime in primes:
        if currnum % prime:
            break

while True:
    cacl()
