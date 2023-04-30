
# string formatting with % #####

# %s is for string
#%d is for integer
#%f is for float values

message = "Hello from %s, I'm learining %s" %("Broadway", "Python")
print(message)
m = "Hello I'm %d years old"%(25)
print(m)

#Fromat() method in string

m = "Hello I'm {}".format("John Doe")
print(m)

m = "i'm {age} years old".format(age=45)
print(m)

#we can also include positions in the placeholder
m = "I have {1}, {0} and {2}".format("pen", "pencil", "book")
print(m)

#if we don't mention the position then the values are taken in order
m= "I have {}, {}, {}".format("pen", "pencil","eraser")
print(m)

# m = "I have {}, {}, {}".format("pen", "pecil") # This gives error because one
# of the place holders can't fill the value

a = "I have {} and {}".format ("pen", "eraser", "pencil") # but thid doesnot give error
print(a)

#m= "I have {0}, {1} and {}".format("pen", "pencil","book") # this gives error
#print(m)

a = "Ihave{item1}, {item2} and {item3}".format(item2="pen", item1="pencil", item3="book")
print(a)

#But positional arugmetn can't be given after a keyword argument in any python functions
# m = "Ihave{item1}, {item2} and {item3}".format(item2="pen", "PENCIL", item3="book")
#this raises error


#F-strings
item1 = "pen"
item2 = "laptop"
item3 = "mouse"

a= f"Ihave{item1}, {item2},{item3}"
print(a)

#WE CAN directly wirte sting  inside the placeholder
m = f"I have {'pen'}, {'penil'} and {'book'}"
print(m)


# F-string are also valid for triple quoted string
a = f"""
I have {item1} and {item2}
"""
print(a)




#### Set Type####

#Set is an unordered data-type in python
#Set is mutable but it's values must be immutable
# We create set using curyly braces for e.g. {1,2,3,"Hello"}
#To create an empty set we use set() built-in fucntion
# Note: {} => This is an empty dictionary and not an empty set
#a = {1,2,3} # non-empty set
a = set() # this is an empty set
# a = {[1,2,3], 3} # this is invalid because it has an mutable type list

# Adding and removng set items

s = {1,2,3} # non-empty set

s.add(4) # This adds 4 in the set at arbitary position
print(s)
s.update([5,6,7]) # This add 5 and 7 in the set
print(s)


