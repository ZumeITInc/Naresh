# keys(): it returns all keys from dict.
dict_one = {1:'python',2:(3+5j),3:(10,20,30),4:[10,'a',False],}
dict_one.keys()
print(dict_one.keys())

# values(): it returns all values from the dict.
print(dict_one.values())

# copy(): it copies the dict into new dict.
dict_two = dict_one.copy()
print(dict_one)
print(dict_two)

# pop(): it removes specific key value pair.
dict_one.pop(1)
print(dict_one)

# Note: we can also remove the key: value pair by using 'del' command.
del dict_one[2]
print(dict_one)

# clear(): it removes all key:value pairs from dict.
dict_one.clear()
print(dict_one)

# fromkeys(): we can use tuple elements as keys in the dict and the elements must be unique
#creating tuple
tup_le = (1,2,3,4)
#taking tuple elements as keys in the dict dic1
print(dict_one.fromkeys(tup_le))


# By default values are None, if we need to get 0 as default then,
print(dict_one.fromkeys(tup_le,0))


#we can also use list elements as keys in the dict and the elements must be unique
# creating list
lst = [1,2,5,]
print(dict_one.fromkeys(lst))

# By default values are None, if we need to get 0 as default then
print(dict_one.fromkeys(lst,1))

# get(): this function is used to get the value of specified key.
stud_details = {'id':101,"Name":"John",'subjects':['AWS','Python','Oracle'],'id':102,"name":'Python'}
print(stud_details.get('id'))
print(stud_details.get('subjects'))


# Items(): this function is used to get all items. All key and value pairs will be displayed in tuple format.
print(stud_details.items())


# Update(): the current dictionary will be updated with the all key:value pairs from another dictionary.
stud_details_one = {'id':103,"name":'Rossum'}
print(stud_details.update(stud_details_one))

# How to perform arithmetic operations on the values of a dictionary?’
d1 = {'sub1':85,"sub2":65,"sub3":78}
print(d1)
sum = sum(d1.values())
print(sum)

max = max(d1.values())
print(max)


min = min(d1.values())
print(min)

le = len(d1.values())
print(le)
