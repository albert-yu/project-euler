# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the 
# square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

def sum_up_to(n):
    return (n * (n + 1)) // 2

def square_of_sum(n):
    return sum_up_to(n) ** 2

def sum_of_squares(n):
    current_sum = 0

    for i in range(1, n + 1):
        current_sum += i**2

    return current_sum

def get_answer(n):
    return abs(square_of_sum(n) - sum_of_squares(n))

def main():
    print(get_answer(100))

if __name__ == "__main__":
    main()

