#! Python 3

# Find the sum of even-valued terms in the Fibonacci sequence below user input number

print("Enter range to sum even Fibonacci sequence")

#initialize total to 0
total = 0
FibMax = int(input())
n = 1
previous = 1
while(n < FibMax):
    print(n)
    if n % 2 == 0:
          total += n
    storeprev = n
    n = n + previous
    previous = storeprev
print("The total sum equals: " + str(total))
