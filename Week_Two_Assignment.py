#Create an empty list called my_list
my_list=[]
#Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10) #output [10]
my_list.append(20) #output [10,20]
my_list.append(30) #output [10,20,30]
my_list.append(40) #output [10,20,30,40]

#Insert the value 15 at the second position in the list
new_element=[50, 60, 70]
my_list.extend(new_element) # output [10, 20, 30, 40, 50, 60, 70]

#Remove the last element from my_list.
del my_list[-1] #output [10, 20, 30, 40, 50, 60]

#Sort my_list in ascending order
my_list.sort() #output [10, 20, 30, 40, 50, 60]

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)
