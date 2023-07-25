from faker import Faker
from random import randint

def print_employees_below_value(sal_list,value):

 fake = Faker()

 employees = [fake.name() for _ in range(1,21)]
employees =['William White', 'Tara Combs', 'Christina Williams', 'Thomas Walker', 'Brian Clark', 'Christine Martin', 'Deanna Jones', 'Nathan Bailey', 'David Allison', 'Craig Friedman', 'Stephen Brown', 'Melinda Davis', 'Chelsey Glenn', 'Christine Williams', 'Thomas Hill', 'Sean Sanders', 'Sandra Reid', 'Jesus Brown', 'James Cook', 'Gregory Floyd']

numbers = [randint(10,70)for _ in range(1,21)]

#append
my_list = ["sravani","harsha"]
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append("S")
print(my_list)

#sort

my_list = [8,3,1,6,]
sorted_list = sorted(my_list)
print(sorted_list)

#extend
my_list = [1,7,5]
my_list.extend([8,4,2])
my_list.extend(["buddi"])
print(my_list)