from problem_3 import is_prime

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def get_primes_less_than(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def get_exponent(prime, multiple):
    # gives the exponent of a prime factor 
    exp = 0
    while multiple % (prime**exp) == 0:
        exp += 1
    return exp - 1


def factors(n):
    """
    @type n: an integer
    @param n: the number we want to factorize
    @rtype: a hash
    @return: the prime factorizations. key = prime, value = exponent (>=1)
    """
    factorization = dict()

    if is_prime(n):
        factorization[n] = 1

    else:
        candidate = 2
        while candidate * candidate <= n:
            # print(candidate)
            if (n % candidate == 0) and is_prime(candidate):  # if evenly divisible and prime
                exponent = get_exponent(candidate, n)
                factorization[candidate] = exponent
                complement = n // candidate ** exponent  # consider complement
                if is_prime(complement):
                    factorization[complement] = 1

            if candidate == 2:
                candidate += 1
            else:
                candidate += 2

    return factorization


def lcm(hash_1, hash_2):
    keys_1 = list(hash_1.keys())
    keys_2 = list(hash_2.keys())
    # returns the least common multiple between two factorization hashes
    joined = keys_1 + keys_2
    new_hash = dict()
    for prime in joined:
        # take care of any primes not shared between the two
        if prime not in hash_1:
            new_hash[prime] = hash_2[prime]
        elif prime not in hash_2:
            new_hash[prime] = hash_1[prime]

        # take care of any shared primes
        else:
            new_hash[prime] = max(hash_1[prime], hash_2[prime])

    return new_hash


def product_of(factorization):
    """
    @type factorization: a hash<int, int>
    @param factorization: key = prime, value = exponent (>=1)
    @rtype: int
    @return: the product
    """
    product = 1
    for prime in factorization.keys():
        new_product = product * prime ** factorization[prime]
        product = new_product

    return product


# gives answer to question concerning 1 to n
def get_answer(n):
    all_factors = range(2, n + 1)
    primes = get_primes_less_than(n)
    composites = list(set(all_factors) - set(primes))

    # to build out our final multiple, we will use hashes to keep track of the prime factorizations
    # and the minimum exponent needed for each prime
    base_factorization = {prime: 1 for prime in primes}  # at least one prime factor for each

    for composite in composites:
        factorization = factors(composite)
        base_factorization = lcm(factorization, base_factorization)

    return product_of(base_factorization)


def main():
    print(get_answer(20))

if __name__ == "__main__":
    main()