# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def is_prime(number):
	if number <= 1:
		return False
	elif number <= 3:
		return True
	elif (number % 2 == 0) or (number % 3 == 0):
		return False
	i = 5
	while i * i <= number:
		if (number % i == 0) or (number % (i+2) == 0):
			return False
		i = i + 6

	return True

def find_largest_p_factor(number):
	# we will assume the number is odd for simplicity's sake

	factor_to_test = 1
	current_candidate = factor_to_test

	while factor_to_test * factor_to_test < number:
		# print(factor_to_test)
		if number % factor_to_test == 0:  # first test if number is a factor at all
			complement = number // factor_to_test
			# print(factor_to_test)
			# print("complement: " + str(complement))
			if is_prime(complement):

				return complement
			elif is_prime(factor_to_test) and (factor_to_test > current_candidate):
				current_candidate = factor_to_test

		factor_to_test += 2  # ignore all even numbers as possible factors

	return current_candidate


def main():
	# print(is_prime(600851475143))
	print(find_largest_p_factor(600851475143))

if __name__ == "__main__":
	main()