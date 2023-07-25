



_var = "vinod"

_num = 123

_float = 1.2




cars = ["mahindra", "tata", "volvo"] # 0, 1, 2




cars[2] = "BMW"

print(cars[2])




details = {"name": "vinod@tessrac.com", "age": 16, "height": 5.7, "address": None, "status": False}

# print(details["age"])




_setvalues = set({'name', 'age', 'address'})

print(_setvalues)




_non_set_values = frozenset(_setvalues)

# _non_set_values[0] = 'status'

# print(_non_set_values)




# for i in range(50, 61):

#     print(i)




def getmyage():

    print(details["age"])




getmyage()




def addAge(age):

    global details




    if isinstance(age, int):

        details['age'] = age

    else:

        raise Exception('give proper input type - only accepts integer')





addAge(24)

print(details)

print(type(details))



print(a.casefold())
print(a.center())
print(a.count())
print(a.encode())
print(a.endswith())
print(a.expandtabs())
print(a.find())
print(a.format())
print(a.format_map())
print(a.index())
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprinatble())
print(a.isspace())
print(a.istitle())
print(a.isipper())
print(a.join())
print(a.ljust())
print(a.lower())
print(a.strip())
print(a.maketrans())
print(a.partition())
print(a.replace())
print(a.rfind())
print(a.rindex())
print(a.rjust())
print(a.rpartition())
print(a.rsplit())
print(a.rstrip())
print(a.split())
print(a.splitlines())
print(a.startswith())
print(a.swapcase())
print(a.title())
print(a.transalte())
print(a.zfill())