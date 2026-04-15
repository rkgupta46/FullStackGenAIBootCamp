import TestShaurya.Test1

def main(arguments):
    print("Hello, " + arguments + "! Welcome to fullstackgenaibootcamp!")
    obj=TestShaurya.Test1
    # Check if a number is prime
    num = int(input("Enter a number to check prime number or not: "))
    print("Is", num, "prime?", obj.is_prime(num))

        # Find primes up to num1
    num1 = int(input("Enter a number to find primes up to: "))
    print("\nPrimes up to " + str(num1) + ":", obj.find_primes(num1))


if __name__ == "__main__":
    main("Ramesh Kumar")
