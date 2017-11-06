from time import sleep, time
from math import sqrt
f = open("resultsPrime.txt", "a")
currnum = 3;
primes = [2]
primes_curr_interval = [2]
x = 0

def calcp():
    global currnum, primes, primes_curr_interval
    for p in primes:
      if p <= sqrt(currnum):
        # currnum += 1
        # return
        if currnum % p == 0:
          # print("HIHIH")
          currnum += 1
          # sleep(5)
          return
    # print(str(currnum))
    primes.append(currnum)
    primes_curr_interval.append(currnum)
    f.write(str(currnum) + "\n")
    currnum += 1
    # sleep(1)

print("START")
while x < 100:
    for i in range(1, 1000):
      calcp()
    print(str(x) + "\t" + str(len(primes_curr_interval)))
    primes_curr_interval = []
    # sleep(.5)
    x += 1
# print("running")
# while x < 50000:
#   start = time()
#   calcp()
#   x += 1
# end = time()
# print("TIME:")
# print(str(end - start))
print("END")
    
