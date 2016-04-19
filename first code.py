random_numbers = [76,23,1,45,7,5,2,1,2,2,2,4,88,66,66,55]
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
