random_numbers = [76,23,1,45,7,5,2,1,2,2,2,4,88,66,66,55,5,12,314,545,777,12,32]
def remove_duplicates(x):
    l=[]
    c=True
    for i in x:
        for j in l:
            if i==j:
                c=False
        if c:
            l.append(i)
        c=True
    return l
print "Sorted and Purified "+str(sorted(remove_duplicates(random_numbers)))


y=raw_input("add or subtract or divide or multiply?")

if y=="add":
	x=int(raw_input("first number"))
	y=int(raw_input("2nd number"))
	print x+y
elif(y=="multiply"):
	x=int(raw_input("first number"))
	y=int(raw_input("2nd number"))
	print x*y
elif(y=="divide"):
	x=int(raw_input("first number"))
	y=int(raw_input("2nd number"))
	print x/y

elif(y=="subtract"):
	x=int(raw_input("first number"))
	y=int(raw_input("2nd number"))
	print x-y


<<<<<<< HEAD

=======
print "Hello world"
>>>>>>> hello
