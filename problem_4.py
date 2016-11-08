# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    string_form = str(number)
    i = 0
    size = len(string_form)
    while i <= size // 2:
        j = size - 1 - i
        if string_form[i] != string_form[j]:
            return False
        i += 1
    return True


def largest_palindrome():
    palindromes = []
    factor_1 = 999
    i = 0
    while factor_1 >= 100:
        factor_2 = factor_1 - i
        found = False
        while factor_2 >= 100 and not found:
            product = factor_1 * factor_2
            if is_palindrome(product):
                palindromes.append(product)
                found = True
            else:
                factor_2 -= 1
        i += 1
        factor_1 -= 1

    return max(palindromes)

def main():
    print(largest_palindrome())

if __name__ == "__main__":
    main()