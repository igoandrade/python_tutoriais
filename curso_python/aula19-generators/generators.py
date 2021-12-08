def generateEvenNumbers(limit):
    num = 1
    while num < limit:
        yield num*2
        num += 1

evenNumbers = generateEvenNumbers(10)
for i in evenNumbers:
    print(i)