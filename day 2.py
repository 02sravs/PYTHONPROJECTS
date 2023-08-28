# count vowels
def vowel_count(input_string):
    vowels = ['a','e','i','o','u']
    vowels_count = 0

    for char in input_string:
        if char in vowels:
              vowels_count += 1

    return vowels_count


input_string = input("Enter a string value: ")

result = vowel_count(input_string)

print("Number of vowels:", result)

#palindrome or not
def is_palindrome(word):
    word = word.replace(" ", "").lower()
return word == word[::-1]

word = input("Enter a word: ")
# Check if the word is a palindrome and display the result
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

#list comprehension

input_numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in input_numbers]

even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

#to find prime or not
def is_prime(number):
    
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("It's a prime number!")
else:
    print("It's not a prime number.")




