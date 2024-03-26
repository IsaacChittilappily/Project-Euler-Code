# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all multiples of 5 or 3 under 1000.

sum = 0

for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        sum += num

print(sum)