# ---COURSE 2 ASSIGNMENT----
# 1a. Write a Python program to check if value 200 exists in the following dictionary.
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# 1b. print the value of key 'history' from the dictionary.
import re


sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

print(sampleDict["class"]["student"]["marks"]["history"])

#1c. 
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

del sample_dict["name"]
del sample_dict["salary"]
print(sample_dict)

# 1d. Write a program to rename a key city to a location in the following dictionary.
sample_dict["city"] = "London"
print(sample_dict)

# Q15. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic4 = {}

for k1, v1 in dic1.items():
    dic4.update({k1 : v1})
for k2, v2 in dic2.items():
    dic4.update({k2 : v2})
for k3, v3 in dic3.items():
    dic4.update({k3 : v3})

print(dic4)

# Q16. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dic5 = {0: 10, 1 : 20}
dic5.update({2 : 30})
print(dic5)

# Q17. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300}
for kd, vd in d1.items():
    if kd in d2:
        d2[kd] += d1[kd]
    else:
        d2.update({kd : vd})
print(d2)

# Q18. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
dic6 = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
s_dic6 = sorted(dic6.items(), key=lambda item: item[1], reverse=True)
for c in range(3):
    print(s_dic6[c])

# Q19. Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)
subs = {'Math':81, 'Physics':83, 'Chemistry':87}
s_subs = sorted(subs.items(), key=lambda item: item[1], reverse=True)
print(s_subs)

# Q20. Write a Python program to convert more than one list to nested dictionary. Go to the editor
# Original strings:
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
score = [85, 98, 89, 92]

dic7 = {}
l = len(ids)
for x in range(l):
    temp = {names[x] : score[x]}
    dic7.update({ids[x] : temp})
print(dic7)

# q21. Write a Python program to remove a specified dictionary from a given list.
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
cols = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
for col in cols:
    for kcol, vcol in col.items():
        if vcol == '#FF0000':
            cols.remove(col)
print(cols)

# q22. Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]
subjs = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

sci_scores = []
for subj in subjs:
    for k, v in subj.items():
        if k == 'Science':
            sci_scores.append(v)
print(sci_scores)

math_scores = []
for subj in subjs:
    for k, v in subj.items():
        if k == 'Math':
            math_scores.append(v)
print(math_scores)


# #Q2. Assume that a user has current balance of 1000, write Python code to simulate a
# # bank transaction where a user tries to make a withdrawal. Your script should accept
# # the amount user wants to withdraw as input. if the amount entered is greater than
# # the current balance output "Insufficient balance" to the user
# # else compute the new balance by deduction the amount entered from the exisiting balance
# # and output this new balance to the user.
# # subtract the amount been withdraw from the current balance and
# # Example: current balance is 1000, if user tries to withdraw 1100
# # this transaction should decline since there is insufficient balance. On the other hand
# # if the user tries to withdraw 100, this transaction should be accepted, and output the
# # new balance that is 900 to the user.


# # Q3. Following the logic in Q2 above, this time around add a condition that
# # allows:
# #    a. the user to enter the pincode (default pin = 2464). if the pincode entered is
# #    wrong output Pincode Invalid.
# #    b. if pincode is correct the user to decide whether to make a withdrawal or check
# #    their balance.
# # Example, enter pincode 2464. If pincode is correct choose option 1 - check balance
# # or option 2 - make withdrawal. If option 1 is selected, output the user's current balance.
# # If option 2 proceed to ask the user the amount they want to withdraw and output the balance.
# # if the option selected is neither 1 nor 2 output selected option does not exist.

account_balance = 1000
pin_code = 2464

pin_str = input('Enter your pin code: ')
pin = int(pin_str)

if pin == pin_code:
    print('Enter 1 to check balance')
    print('Enter 2 to withdraw an amount')
    option = input('Enter option : ')
    if option == '1':
        print(f'Your current balance is {account_balance}')
    elif option == '2':
        amount_str = input('Enter an amount: ')
        amount = int(amount_str)
        if amount > account_balance:
            print('Insufficent balance')
        else:
            account_balance = account_balance - amount
            print(f'Your new balance is {account_balance}')
    else:
        print('Invalid option')
else:
    print('Invalid pin code')

# Final Project 1:
# Write a full bank application using Python (use functions for your solution). Your application should allow the following:
# Check if user already register? if not,
#     a. get firstname and lastname of user. Put a condition to check to make sure that both firstname and lastname are not empty
#     b. 4 digit pincode.  Use the digits as the key and store
#     firstname, lastname and 4 digit as pincode. Put a condition to check if:
#         i. the characters entered are of length 4.
#         ii. the digits are not part of the existing keys (no duplicate keys allowed). Store the keys as strings (see sample user information below)
#     c. set default current balance for new registered users as 0
# if a user is already registered, perform these:
#     1. Gets pincode from user. Checks if pincode is correct, by cross-checking it in users info dictionary. If not, allow the user
#     to try again for 3 times and block the user for trying again afterwards.

#     2. If pincode is correct display options to decide whether to make a withdrawal, check
#     account balance or deposit money.
#     If 'withdrawal' option:
#         a. allow user to enter amount.
#         b. check whether amount entered is less than or equal to user's current balance. This can be found in the user information dictionary.
#         If true deduct this amount from the current balance, update the user balance info in the dictionary and display the new balance to the user,
#         else output 'insufficient balance'

#     If the user selects 'check balance' option:
#         a. get the user balance from the dictionary and display it to the user.
#     If the user selects 'deposit money' option:
#         a. allow user to enter amount to be deposited
#         b. update the user balance information in the dictionary and display the new balance to the user

user_information = {
    '7563' : {'firstname': 'Jeremy', 'lastname':'Johnson', 'current_balance': 1_000_000_000_000, 'pincode':7563},
    '7576' : {'firstname': 'Kwame', 'lastname':'Kumah', 'current_balance': 90_000_000, 'pincode':7576},
    '4475' : {'firstname': 'Peter', 'lastname':'Asamoah', 'current_balance': 65_000_000, 'pincode':4475},
    '4005' : {'firstname': 'Akwasi', 'lastname':'Brobe', 'current_balance': 4_000_000, 'pincode':4005},
    '4476' : {'firstname': 'Yaw', 'lastname':'Ofosu', 'current_balance': 105_000_000, 'pincode':4475},
    '3543' : {'firstname': 'Samantha', 'lastname':'Luz', 'current_balance': 2_905_000_000, 'pincode':3543},
    '3544' : {'firstname': 'Goods', 'lastname':'Mode', 'current_balance': 0, 'pincode':3543}
}

def execute_bank_workflow():
    print('Enter 1 to register an account')
    print('Enter 2 to enter your account')
    print('Enter anything else to exit')
    start = input('Enter number: ')

    if start == '1':
        handle_new_user()
    elif start == '2':
        handle_existing_user()
    else:
        print('Thanks. Goodbye')

def handle_new_user():
    firstname = input('Enter first name: ')
    lastname = input('Enter last name: ')

    while len(firstname) < 0 and len(lastname) < 0:
        firstname = input('Please provide a valid first name: ')
        lastname = input('Please provide a valid last name: ')
    
    pincode = input('Enter a pin code: ')
    retry = 0    
    while (pincode in user_information or len(pincode) < 4) and retry < 3:
        pincode = input('Please provide a valid pin code: ')
        retry = retry + 1
    
    if retry == 3:
        print('User registration failed')
    else:
        user_information[pincode] = { 
            "firstname": firstname,
            "lastname": lastname,
            "current_balance": 0,
            "pincode": int(pincode)
        }
        print(f'Registration complete for {firstname} {lastname}')

def handle_existing_user():
    pincode = input('Enter your pincode: ')
    retry = 0
    while pincode not in user_information and retry < 3:
        pincode = input('Invalid pin code please try again: ')
        retry = retry + 1
    
    if retry == 3:
        print('Failed to authenticate')
    else:
        user = user_information[pincode]
        print('Enter 1 to make a withdrawal')
        print('Enter 2 to make a deposit')
        print('Enter 3 to check your balance')
        print('Enter anything else to exit')
        option = input('Enter option: ')

        if option == '1':            
            handle_withdrawal(user)
        elif option == '2':
            handle_deposit(user)
        elif option == '3':
            handle_check_balance(user)
        else:
            print('Thanks. Goodbye')
        
def handle_withdrawal(user):
    amount_str = input('Enter Amount: ')
    amount = int(amount_str)
    user['current_balance'] = user['current_balance'] - amount
    balance = user['current_balance']
    print(f'Your current balance is {balance}')

def handle_deposit(user):
    amount_str = input('Enter Amount: ')
    amount = int(amount_str)
    user['current_balance'] = user['current_balance'] + amount
    balance = user['current_balance']
    print(f'Your current balance is {balance}')

def handle_check_balance(user):
    balance = user['current_balance']
    print(f'Your current balance is {balance}')

execute_bank_workflow()