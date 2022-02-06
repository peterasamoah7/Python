#---------try, except, else, finally----#
try:
    dic = { 'Age': 1}
    print(dic['Age'])
except TypeError as e:
    print('Caught type error')
except ValueError as e:
    print('Caught value error')
except KeyError as e:
    print(f'Missing key: {e}')
except Exception as e:
    print(e) #for logging
    print('You cannot add a string and an integer') #for users
else:
    dic['Age'] = 31
    print(dic['Age']) #block only runs when try block doesn't error
finally:
    print('I always run') #code block always executes