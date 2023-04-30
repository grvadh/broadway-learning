s = {
    "name": "jon",
    "email": "jon@gmail.com",
    "address": "KTM"
}

## all() built-in function. This function takes iterable(sequence) as a
# parameter and returns True if all the elements of the sequence are truthy. In case of dictionary
# it checks the key of the dictionary

print(all(s)) # it gives True as all the keys of the dictionary (name, email, address) are truthy.
print(all([])) # this is an exception in the all() function because it returns True.

a= {"": 1} # this is a valid dectionary. An empty string is a key with value 1
print(all(a)) # This returns False beacause the dictionary has a Flasy key



#### any() built-in functions  also takes iterable (sequence) as a parameter. But it returns True
# if at least one of the elements is Truthy
b = {0: "Hello", 1:"World"}
any(b) # This returns True because one of the keys (i.e. 1) is Truthy

#But if all the keys are Falsy then it returns False
b = {"":"Hello", 0:"World"}
print(any(b)) # This returns False


student = {"name": "Jon", "age": 23}
print(sorted(student)) # it sort the keys of the dictionary in alpahabetical order.
# it returns list ["age", "name"]

print(str(student))
print(type(student))
