def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        Boolean: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_primes(limit):
    """
    Find all prime numbers up to a given limit.
    
    Args:
        limit: Upper bound for finding primes
        
    Returns:
        List of all prime numbers up to limit
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def sieve_of_eratosthenes(limit):
    """
    Find all primes up to a limit using Sieve of Eratosthenes (efficient method).
    
    Args:
        limit: Upper bound for finding primes
        
    Returns:
        List of all prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Create a boolean array and mark all as true
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime_arr[i]:
            # Mark multiples as not prime
            for j in range(i*i, limit + 1, i):
                is_prime_arr[j] = False
    
    # Collect all prime numbers
    return [num for num in range(2, limit + 1) if is_prime_arr[num]]