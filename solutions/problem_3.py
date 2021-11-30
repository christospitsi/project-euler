def prime_factors(n):
    """
    Loop starts at the first prime (d=2) and removes all factors.
    d will always be a prime if n % d == 0. Say n = 120. 120's prime factors are 2,2,2,3,5. 
    When d = 2, the (while n % d == 0) strips all 2's from the number, we are left with some other prime factors. 
    Those prime factors will be larger than 2. 
    The loop terminates at sqrt(n), because there cannot be any prime factors larger than sqrt(n)."""

    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs) # The largest element in the prime factor list
