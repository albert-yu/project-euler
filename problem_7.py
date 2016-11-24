from problem_3 import is_prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def nth_prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3

    primes_found_so_far = 2
    current_num = 5
    while primes_found_so_far < n:
        if is_prime(current_num):
            primes_found_so_far += 1
        current_num += 2

    return current_num - 2

def main():
    print(nth_prime(10001))


if __name__ == "__main__":
    main()