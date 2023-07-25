#event nums = []

#loop - 1-100

#if condition - check even num

#add even num to that list

#print(even nums list)

even_numbers=[]
for num in range(1,100):
  if num % 2 ==0:
    even_numbers.append(num)

print(even_numbers)

#odd num
odd_num=[]
for num in range(1,100):
  if num%2 !=0:
    odd_num.append(num)

print(odd_num)

#prime numbers
def is_prime(number):

 lower_limit = 1
upper_limit = 100
prime_num=[]
for num in range(lower_limit, upper_limit + 1):
  if is_prime(num): 
    prime_num.append(num)

print(prime_num)

#
