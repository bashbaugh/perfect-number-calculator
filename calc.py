#Benjamin's perfect number calculator

currnum = 1

with open("results.txt", "a") as f:
    f.write("perfect numbers:")


def calculate():
    global currnum
    if currnum % 6 == 0:
      currnum = currnum
    divisors = []
    for x in range (1, currnum - 1):
        if currnum % x == 0:
            divisors.append(x)
    divs_added = sum(divisors)
    if currnum == divs_added:
        print ("perfect number found: " + str(currnum))
        with open("results.txt", "a") as f:
            f.write("\n " + str(currnum))
    currnum += 1

while True:
     hvgh = calculate()
