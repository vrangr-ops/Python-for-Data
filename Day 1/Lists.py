#lists
#Lists are ordered, mutable and allow duplicate values.


coaches_list = ["sam", "ollie","luke","jef","Tom"]
print(coaches_list)
print(len(coaches_list))

#list indexing= n-1

print(coaches_list[2])

#up to 3rd element
print (coaches_list[0:3])

#First 2 elements
print (coaches_list[:2])

#see if something exists in the list( case sensitive)
print ("sam" in coaches_list)
print ("burhan" in coaches_list)

#change value of an item in the list
coaches_list[1] ="burhan" 

print (coaches_list)

#change the list with multiple items
coaches_list[1:2] = {"Alan","Barney"}
print (coaches_list)
print (len(coaches_list))

print ("------------------------------------------------")

#   Negative index
print("the last coach is ", coaches_list[-1])

print ("The third last coach is" , coaches_list[-3])

x= "cool"

print (x[3] + x[1] +x[0]+ x[1])
print(x[-1] + x[-2] + x[-4] + x[-3]) # loco

print ("------------------------------------------------")
# List methods
num_list = [1, 2, 3, 4, 5, 43, 7, 3, 6, 3, 7, 2, 44, 21, 12, 98]

print(num_list)

# insert a number in specific position
num_list.insert(2, 450)

# remove item at index
num_list.pop(7)
print(num_list)

# sort list, largest to smallest
num_list.sort(reverse=True)
print(num_list)

# add item to end of list
num_list.append(7)
print(num_list)


print ("------------------------------------------------")
#slicing
#list[initial :end:IndexStep]
#can be done on lists,strings and tuples
my_list =[20,30,40,50,60,70]

#inital is inclusive , end is exclusive
print (my_list[1:4])
#negative slicing
print (my_list[-5::1])
       
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums_even = nums[1::2]

print(nums_even)


#List as arrays -store only numbers

import array as arr

my_arr = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print(my_arr)

