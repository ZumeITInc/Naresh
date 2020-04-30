# programs on list
l1 = [10,20,60,480,20]
print(l1[-1])
l1[2] = 45
print(l1)

# EXAMPLE ON hetrogenious data
l1 = [10,"Django",18500.02,False]
print(l1)
print(l1[2])
print(l1[-2])

# example on using + operator on a list
l1 = [10,25,45,87]
l2 = [24,57,86,45]
l3 = l1+l2
print(l1)
print(l2)
print(l3)

# example of + opeartor on list
a1 = [10,25,45,12]
a2 = [45,"JohnRossum",10.25]
a3 = a1+a2
print(a1)
print(a2)
print(a3)


# example on multiple operator
l1 = [10,20,30]
l2 = l1 * 3
print(l1)
print(l2)
l3 = [10,54,45]
l4 = [75,84,63]
l5 = [l3*2],[l4*2]
print(l3)
print(l4)
print(l5)


# example 2
a1 = ["Python",10,False]
a2 = a1 * 2
print(a1)
print(a2)

# using built in functions on list
name = input("enter name:")
stud_id = int(input("Enter student id no:"))
marks = [86,85,75,98,89,79]
print("the subjects=",len(marks))
print("total marks=",sum(marks))
print( "max marks=",max(marks))
print( "min marks=",min(marks))
print("type of marks=",type(marks))

# using slice : operator on list
l1=[10,20,30,40,50,60,70,80,90,100]
print(l1[0])
print(l1[-1])
print(l1[0:3])
print(l1[0:9:2])
print(l1[5:0:-1])

# to print list in reverse order
l1 = (l1[::-1])
print(l1[-5:1:-1])

# nested list
l1 = [[10,20],[30,40,50],[60]]
print(l1[0][0])
print(l1[1][-1])
print(l1[0])

# another example
l1 = [[0]*6]
print(l1)
l2 = [[3]+[3],[3]*3,[10,20]]
print(l2)
l3 = [[1,2,3]*3,"python"*2,[4,5]+[1,2,3]*2]
print(l3)
