#multiline string
multiline_string = '''Hi! this is sravani.
completed my b.tech in the stream of IT in vvit.
planning to do ms in Us.
i'm BTS army.'''
print(multiline_string)

#strings as array
a = "Hello Army"
print(a[3])

#string length
a = "This is himavari"
print(len(a))

#check string
txt = "little things in life matters"
print("life" in txt)

#slicing 
a="slicing string"
print(a[4:7])
print(a[:5])
print(a[3:])
print(a[-3:-7])

#modify string
a = "modify string"
print(a.upper())
print(a.lower())
print(a.split())
print(a.replace('f','t'))

#concatenation
a= "2"
b="7"
c=a+b
print(c)

#format
height='5'
txt="i'm himavari and my height is {}"
print(txt.format(height))

#string methods
a = "THESE these string method."
print(a.capitalize())
print(a.casefold())
print(a.endswith("."))
print(a.count("these"))
print(a.encode())
print(a.expandtabs())
print(a.isalnum())
print(a.swapcase())
txt = "50"

x = txt.zfill(8)

print(x)
text = "Hello, world!"
width=20
center_text=text.center(width)
print(center_text)


num=[1,101]
if num % 2 ==0:
  print(num)
else:
  print(odd)