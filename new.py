def count_vowels(input_string):
 vowels= "aeiouAEIOU"

vowels_count =0
for char in input_string:
    if char in vowels:
       vowels_count += 1

return vowels_count

input_string =input("enter the string")
result = vowels_count(input_string)
print("no.of vowels:", result) 