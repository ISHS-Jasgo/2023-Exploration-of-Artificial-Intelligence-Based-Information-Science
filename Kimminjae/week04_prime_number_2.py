# week04 prime_number v1.2
# add is_prime function
# modified by minjae Kim
import primenumber

numbers = sorted(map(int, input("Enter starting number and ending number : ").split()))

for k in range(numbers[0], numbers[1] + 1):
    if primenumber.is_prime(k):
        print(k, end=' ')
