# Use this test list to answer the questions below:
test_list = [ 1, 4, 5, 7, 8, 100, 87, 1037, 90.129, 83, 190, 100] 

# Q1. Write a Python code to find (use string format described above to output your values):
#     a. the smallest and largest values of the list.
print(min(test_list))
print(max(test_list))

#     b. find the length of list.
print(len(test_list))

#     c. convert the list into a string using sparated by '?'
str_list = []
for item in test_list:
    str_list.append(str(item))
print('?'.join(str_list))

#     d. find the index of last element in the list.
item_index = test_list.index(test_list[-1])
print(item_index)

#     e. sort the list in ascending order
test_list.sort()
print(test_list)

#     f. use the sorted function to sort list in descending order
desc = sorted(test_list, reverse=True)
print(desc)

#     g. append values [10098, 2097, 1498] to the front of the list
append_list = [10098, 2097, 1498]
append_list.extend(test_list)
print(append_list)

#     h. get values from index 3 to 7
print(test_list[3:8])

#     i. remove duplicates from the list
unique_list = set(test_list)
print(unique_list)

#     j. print the index and value of the list starting from 1
for i, j in enumerate(test_list):
    print(i, j)

#     l. find the sum of values in the list
print(sum(test_list))

#     m. multiply all values in the list
product = 1
for val in test_list:
    product = product * val
print(product)

# Q2. Why are List mutable and set immutable. Write a python script to emulate this concept.
first_list = [1, 2, 3]
sec_list = first_list
sec_list.append(4)
print(first_list) 
print(sec_list)

first_set = { 1, 2, 3 }
second_set = { 3, 4, 5 }
first_set.add(6)
print(first_set)

# Q3.Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(tuple_list, key=lambda item: item[1])
print(sorted_list)

# Q4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_list.pop(0)
color_list.pop(4 - 1)
color_list.pop(5 - 2)
print(color_list)

# Q5. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
num_clist = []
l_list = ['p', 'q']
#need to discuss

# Q6. Write a Python program to convert a list of multiple integers into a single integer. 
# Sample list: [11, 33, 50]
# Expected Output: 113350
int_list = [11, 33, 50]
int_str = ''
for value in int_list:
    int_str += str(value)
print(int_str)


# Q7. Write a Python program to compute the difference between two lists. 
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
list_1 = ["red", "orange", "green", "blue", "white"]
list_2 = ["black", "yellow", "green", "blue"]
set_1 = set(list_1)
set_2 = set(list_2)
diff_1 = set_1.difference(set_2)
diff_2 = set_2.difference(set_1)
print(diff_1)
print(diff_2)

# Q8. Write a Python program to find the items starts with specific character from a given list. 
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# []
letter_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
word_list = []
for l in letter_list:
    if l.startswith('a'):
        word_list.append(l)
print(word_list)


# Q9.  Write a Python program to extract a specified column from a given nested list. Go to the editor
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]
nested_list = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
col_list = []
for n in nested_list:
    col_list.append(n[0])
print(col_list)

# q10. Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648
mul_tuple = (4, 3, 2, 2, -1, 18)
m = 1
for t in mul_tuple:
   m = m * t
print(m)

# q11. Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
list_tuple = [(1, 2), (2, 3), (3, 4)]
new_list = []
for lt in list_tuple:
    new_list.append(list(lt))
print(new_list)

# q12. Write a Python program to check if a specified element presents in a tuple of tuples. Go to the editor
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False
double_tuple = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
for dt in double_tuple:
    tl = list(dt)
    for cl in tl:
        if cl == 'Olive':
            print('True')
    
    

# q13. Write a Python program to sort a tuple by its float element (desending order)
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
item_tuple =  [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
t_list = list(item_tuple)
s_t_list = sorted(t_list, key=lambda item: item[1], reverse=True)
print(s_t_list)

# q14. Write a Python program to check if two given sets have no elements in common.
set_01 = { 1, 2, 3 }
set_02 = { 1, 2, 3 }
diff = set_01.intersection(set_02)
print(diff)