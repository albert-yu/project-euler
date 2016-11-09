from problem_3 import is_prime

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def get_primes_less_than(n):
	primes = []
	for i in range(2, n + 1):
		if is_prime(i):
			primes.append(i)
	return primes


# gives answer to question concerning 1 to n
def least_common_multiple(n):
	all_factors = range(2, n + 1)
	primes = get_primes_less_than(n)
	composites = list(set(all_factors) - set(primes))

	# to build out our final multiple, we will use hashes to keep track of the prime factorizations
	# and the minimum exponent needed for each prime
	p_factorization = {prime: 1 for prime in primes}  # at least one prime factor for each



def main():
	print(least_common_multiple(20))

if __name__ == "__main__":
	main()