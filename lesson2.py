# #--------Dictionaries----------#
# dict = { 'A' : '1', 'B' : '2', 'C' : 3, 4 : 5, 'Five': ['5'] }
# print(dict['A']) #print 1
# print(dict[4]) #print 5
# print(dict['Five']) #print ['5']
# print(dict.get('none')) #print None
# print(dict.get('none', 'Not found!')) #print None
# #print(dict[6]) #Key error, key doesn't exist
# dict[4] = 4
# print(dict[4]) #print 4 after update
# dict.update({ 'A' : 'a', 'B' : '2', 'c' : 3, 4 : 6, 'Five': ['6'] }) #create new if not existing, update if it does
# del dict[4] #delete value with key 4
# popped = dict.pop('Five') #remove value with key Five
# print(popped) #print popped value
# print(len(dict)) #number of keys
# print(dict.keys()) #get all keys
# print(dict.values()) #get all values
# print(dict.items()) #get a tuple of keys and values
# for k, v in dict.items(): #loop through a dictionary
#     print(k, v)
# print(dict)

# #-----------Control(if, else etc)----------#
# name = 'Peter'
# if name == 'Peter':
#     print(name)
# print(name == 'Peter')
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b) #compares values
# print(a is b) #compares id in memory
# print(id(a)) #id in memory of a
# print(id(b)) #id in memory of b

# #-------------and, or not --------------------#
# user = 'Admin'
# logged_in = True
# if user == 'Admin' and logged_in:
#     print('Admin page')
# else:
#     print('Bad credentials')

# user = 'Admin'
# logged_in = False
# if user == 'Admin' or logged_in:
#     print('Admin page')
# else:
#     print('Bad credentials')

# if 'jeremy' != 'peter':
#     print('True')

# if not logged_in:
#     print('Not logged in')

# #------------False---------#
# con_none = None ## all False
# con_false = False ## ---->
# con_zero = 0 ### ----->
# con_empty_list = [] ### --->
# con_empty_tuple = {} ### ---->


# #----------Input----------#
# # input_value = input('Enter a value: ')
# # print(input_value)

# #---------Loops & Interaction--------#
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 1:
#         print(num)
#         break
#     else:
#         continue    

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(2, 15, 2):
#     print(i)

# x = 0
# while x < 10:
#     print(x)
#     x = x + 1

#---------Functions-----------#
# def first_func(param):
#     print(f'my {param} function')

# first_func('first')
# first_func('second')
# first_func('third')

# def return_function():
#     return 'First return function'

# fn = return_function()
# print(fn)

# def default_param(name ,age=30):
#     return f'{name} is {age} yrs old'

# print(default_param('Peter'))
# print(default_param('Sylvia', '32'))

# def some_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# some_info('Tesla', 'Audi', Year=2022, Mode='Electric')

# def sum_nums(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# n = [100, 200, 300]
# sum_nums(100, 200, 300)
# sum_nums(*n)