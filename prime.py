from time import sleep
f = open("resultsPrime.txt", "a")
currnum = 3;
primes = [2]

def calc():
    global currnum, primes
    for prime in primes:
        if currnum % prime == 0:
            # print("HIHIH")
            currnum += 1
            # sleep(5)
            return
    print(str(currnum))
    primes.append(currnum)
    f.write(str(currnum) + "\n")
    currnum += 1
    # sleep(1)

while True:
    calc()
