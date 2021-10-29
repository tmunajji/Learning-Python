# Ints (Whole #s) and floats (decimals)
print("Ints and Floats:\n")
num1 = 5
num2 = 6.2  # Or written as: float(6.2)
numt = num1 + num2  # You can add ints and floats
print(numt)

# Sumltaneous assignment [Can mix floats and ints, each variable will hold its type, won't mess up]
print("\nSimultaneous Ints and Floats:\n")
a, b, c = 3.0, 1, 2
print(a+b+c)
print(a)
print(b)
print(c)

#Testing Lists - Looks like arrays
print("\nLists:\n")
tlist = []
tlist.append(2)
tlist.append(4)
tlist.append(6)
tlist.append(8)
tlist.append(10)

# Not sure how, but x makes it print everything out in the for()
# Or print manually by putting: print(tlist[0...])
for x in tlist:
    print(x)

mylist = [1,2,3,4,5,6,7,8,9,10]
for x in mylist:
    print(x)

# More List Testing (Prints in order of list - Does not ADD) [Prints within Brackets]
print("\nLists using [] and adding variables:\n")
evenNum = [2,4,6,8,10]
oddNum = [1,3,5,7,9]
allNum = oddNum + evenNum
print(allNum)

# Can multiply String
print("\nMultiply Strings (Repeated String):\n")
manyhello = "hello " * 5
print(manyhello)

# Allows you to place string and numbers by using % in location: %s - string, %d - int, %f - floats, %<#ofdigits>.f - floats with fixed # digits to the right of dot [Tuples]
print("\nTesting Tuples (%):\n")
tupletests = "age"
tupletestd = 19
print("Hello, my %s is %d!" % (tupletests, tupletestd))

# Use %s to print non-string as string
print("Non-String as String Using %s")
testlist = [1,3,5]
print("Print list: %s" % testlist)


