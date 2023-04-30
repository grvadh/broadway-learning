#Accessing dictionary values

student = {"name": "jon", "age": 23, "department" : "CS"}

print(student["name"]) #this gives Jon
print(student["age"]) # this gives 23
#print(student["id"]) #this raises key error


#We can also use get() method in dictionary to access the value
print(student.get("name")) # This also gives Jon

#But if the key is not present in the dictionary  then it gives None
print(student.get("id",3)) # THis gives value 3 for the id key

#But if we gvie default value to the key aleady present in the dictionary,
#it ignores the default value
print(student.get("name","jane")) #it gives jon and the vaalue jane is ignore


### Adding and updating dictionary values

#if the key id is not present in the deictionary then it adds the key and assign
#the value 4

student["id"] = 4 
print(student)

#if te key id is already present in the dictionary then it updates the value in the id,
#in this case 5
student["id"] = 5
student["name"] ="jane" # name in the dictionary jon is updated to Jane


#we can also use update() method to update the existing dictionary
further_info = {"email": "jane@gmail.com", "address": "Kalanki"}
# this gives {name": "jane", "age": 23, "depatment": "CS", "id":5, "email": "jane@gmail.com", "address": "kalanki"}
student.update(further_info)
print(student)

######## Removing items from the dictionary

#pop() method takes key as a prameter. It removes the provided key -value pair from the dictionary
#returns the value
a = student.pop("address") #thsi pops out the address fro mteh dictionary and value is
#assigned to the 'a' vaiable
print(student)
print(a)

#if we try to pop out the key not present in the dictionary then it raises key error

## student.pop("height") # this raises error because "height" key is not present in the dictionary

#But we can assign a default value
height = student.pop("height", 5.9) #this gives 5.9 in the height variable
print(height)


data = student.popitem() # this pops out the last key-value pair from the dictionary and returns
#a(key,value) tuple
print(data) # result will be ("address", "Kalanki")



#student.clear() #clears out the dictionary elements
#del_student # delete the dictionary object.


#Restriction in ictionary keys

# 1. Dectionary keys must be immutable
# 2. Tuples can be used as the dictionary until it has any mutable values

a = {(1,2): 1} # this is valid
#a = {(1, [1,2]): 2} # this is invalid





