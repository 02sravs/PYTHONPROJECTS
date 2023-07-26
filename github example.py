def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

if __name__ == "__main__":
    try:
        start_range = int(input("Enter the starting range: "))
        end_range = int(input("Enter the ending range: "))
        print("Prime numbers between", start_range, "and", end_range, "are:")
        print_primes(start_range, end_range)
    except ValueError:
        print("Invalid input. Please enter valid integer values for the range.")
