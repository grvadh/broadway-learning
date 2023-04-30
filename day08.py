#

#result = a.split() #thsi splits the string with space and returns a list
# a=> ["Hello", "World.", "I'm", "Learning", "Python"]
#print(result)


#Join() is a string method that join the elements of a list by the string which
# calls the join()
messages = ["Hello", "World"]
" ".join(messages)# "Hello World"
"+".join(messages) #"Hello+World"
print(messages)

a = "Hello World. I'm learning Python"
a.find("World") # This searches 'World' in the string and returns the index where
#it finds the 'World'. In this case 6

a.find('o') # thsi gives 4 as 'o' first occurs in 4th position
a.find('o', 5) # This searches 'o' from the 5tht index. Thus, it returns 6


a.replace("Hello", "hello")


# string formatting with %#####
