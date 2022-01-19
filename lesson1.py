print('Lesson 1 - 19th January 2022')

#------Strings--------#
# msg = "Learning python is fun"
# print(msg)

#a function with triple strings
#def sum_():
#    """function to sum numbers"""

#print(help(sum_))
#print(type(msg))
#print(msg[0]) #prints the first character
#print(msg[0:5]) #prints the first n(n = 5 here) characters
#print(msg[2:3]) #prints the n chars from m to n characters
#print(len(msg)) #string length
#print(msg.count('o')) #strin counting
#print(dir(msg)) #directory
#print(help(str)) #help 
#print(msg.upper()) #string lower case method
#print(msg.lower()) #string upper case method
#firstname = 'Peter'
#lastname = 'Asamoah'
#print(f'Hello, {firstname} {lastname}') #string concantenation
#print('Hello, {} {}'.format(firstname, lastname))

#------Numerical-------#
# integer = 3
# dec = 1.32

# print(type(integer))
# print(type(dec))
# print(4 * 3 + 1)
# print(4 * (3 + 1))
# print(3 ** 3)
# print(3 // 2)
# print(4 % 2)
# num = 1
# num += 2
# print(num)
# num *= 2
# print(num)
# print(abs(-3))
# print(round(3.765, 0))
# print(round(3.765, 1))
# print(round(3.765, 2))
# num_1 = int('100')
# num_2 = int('200')
# print(num_1 + num_2)
# print(int(4.56))
# print(float('4.56'))

#------------List-----------#
#titles = ['Mr', 'Ms', 'Mrs', 'Miss', 'Dr', 'Madam', 'Professor']
#list_nums = [1, 3, 4, 5, 6, 7, 8, 9, 0, 2]
# print(titles) #print list as it is
# print(len(titles)) #get length of list
# print(titles[0]) #get first item
# print(titles[len(titles) - 1]) #get last item
# print(titles[-1]) #get last item
#print(titles[20]) #throws an index out of range error
#print(titles[1:4]) #list slicing
#print(titles[0: len(titles): 2]) #list slicing with incremental
#print(titles[2:]) #start slicing from index 2
# titles.append('Emiretus') #adds an object at the end of the list
# titles.insert(1, 'Master') #inserts an object at an index in the list
# another_list = ['Comissioner', 'Baron', 'Baroness', 'King', 'Queen'] # a new list
# titles.extend(another_list) #merge another list into exsting list
# titles.remove('Master') #remove the Master string from the list
# titles.pop() #remove the last object in the list
# titles.reverse() #reveres the objects in the list
# titles.sort() #sort a list
# list_nums.sort() #sort a list
# print(list_nums)
# sorted(list_nums) #reverse False = descending 
# print(max(list_nums)) #max of item
# print(min(list_nums)) #min of item
# print(sum(list_nums)) #sum of items in list
# print(titles.index('Mr')) #get index of existing item
# print(titles)
# if 'Mr' in titles:
#     print('Mr is here!')
# for title in titles:
#     print(title)
# for index, title in enumerate(titles):
#     print(index, title)
# titles_str = '<-->'.join(titles)
# print(titles_str)
# split_str = titles_str.split('<-->')
# print(split_str)
#titles_copy = titles[:] #create a copy
#empty_list = [] 
#empty_list = list()

#----------Tuples------------#
# titles_tuple = ('Mr', 'Mrs', 'Dr', 'Ms', 'Miss')
# print(titles_tuple)
#empty_tuple = ()
#empty_tuple = tuple()

#----------Sets------------#
# num_set = { 1, 2, 3, 5, 6, 7, 8, 9 }
# num_set2 = { 1, 2, 3, 5 }
# print(num_set)
# print(num_set2)
# print(num_set.intersection(num_set2))
# print(num_set.difference(num_set2))
# print(num_set.union(num_set2))
# list_nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
# print(set(list_nums))
#empty_set = set() #create a new set
#empty_set.add(1) #add a value to a set
#print(empty_set) #print the set