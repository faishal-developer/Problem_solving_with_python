import turtle
# import camelcase
f=open("slidingWindowMaximum.py",'r')
print(f.read(),'f')

print(5/2)
# marks = input("give marks:")
# print(float(marks)+2)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(145)
# turtle.forward(122)
# turtle.left(120)
# turtle.forward(20)
# turtle.shape("turtle")
# turtle.exitonclick()
"""kdjfkdf
dkdjfkd
dfdfk"""
# finding type
print(type([])== list)
# type casting
print(int(2.8))
print(float('2.0'))
print(str(23))

# multi line string
str="""
    thiS is my ona
    and my multiline string 
    testing
"""
str2=''' this 
is 
als o
    kk'''
print("also" not in str) #in js-------=> !str.includes("also")
print(str2[-5:-1]) #in js this is str.slice(0,5)
print(str2[:5].upper()) #in js this is toUpperCase()
# print(str2.strip()) #in js this is .trim()
# print(str2.replace("i","z")) #in js str2.replace('i','z')
# number and string concatenation
age=30.126456
str3="mdFaishal"
txt=f"{str3} {age:.2f}"
print(txt)
# escape charecters
txt2="md Faishal \"vikings\" md"
print(txt2.capitalize())
print(txt2.lower())
print(txt.translate('bengali'),"--------->")

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))
arr=[1,2,3,4]
print(arr[:1]+arr[2:])