#using curly braces
s={1,2,3,4}
#using set() functions
s2=set([1,2,2,3])
#Adding elements in set
s.add(4)
#Removing elements
s.remove(1)#error if element not found
s.discard(5)#no error if element not found
s.pop()
print(s)
