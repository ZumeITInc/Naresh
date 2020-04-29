# Creating empty dictionary and adding key:value pairs.
dict1 = {}
print(dict1)
print(type(dict1))

#adding Key:Value pair to dictionary
dict1['a'] = 10
print(dict1)
dict1['b'] = 25
print(dict1)
dict1['c'] = 36
print(dict1)

#trying to add same Key:value pair
dict1['a'] = 10
print(dict1)

#adding new value for same key ‘a’
dict1['a'] = 50
print(dict1)

# To avoid confusion just separating the line
print('=======================================')

# Creating a dictionary with dict() function
dict_one = dict([('x',12),("y",65),('z',45)])
print(dict_one)

# Creating a dictionary with curly braces including key:value pairs
dict_one = {'p':12,'y':15,'t':35}
print(dict_one)
print(type(dict_one))

# Accessing data from dictionary
# We can assign values to the keys and later we can fetch values by using Keys
stud_details = {'id':101,"Name":"Mahesh",'Age':24,'marks':425}
print(stud_details)
print(type(stud_details))
print(stud_details["id"])
print(stud_details["Name"])

# Another Example
stud_details = {'id':102,"Name":'Scorpio',"Subjects":['SQL Server','Python','Oracle','AWS']}
print(stud_details)
print(type(stud_details))
print(stud_details['id'])
print(stud_details['Subjects'])

# print(stud_details['age'])
# To prevent this type of error we can check whether the specified key existed or not by using has_key().
# In python3 we have to check by using membership operator ‘in’
'age' in stud_details

# Adding new key:value pairs
stud_details['age'] = 24
print(stud_details)

# Updating dictionary values
#changing the age from 24 to 27
stud_details['age'] = 27
print(stud_details)

# Deleting key:value pairs from dictionary
# If we need to delete the value 27 from the above dictionary then (by using pop)
stud_details.pop('age')
print(stud_details)

# We can also delete by using popitem()
#this function removes last key:value pair in the dictionary,
stud_details.popitem()
print(stud_details)






