def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# 2から100までの素数を列挙
primes_2_to_100 = list_primes(2, 100)
print(primes_2_to_100)
