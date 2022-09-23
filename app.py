test = 4
test2 = 'Hello'

try:
    #code that may crash 
    test3 = test + test2
    # specific error catch
except TypeError:
    print('Can not add a string to a number')
     # general error catch
except:
    print('Error')
    # a catch all wether error or not
finally:
    print('okie dokie')



def user_input():
    user_input = input("pick a number: ")
    try:    
        user_input = float(user_input)
    except:
        print('try again')
    return user_input

result = user_input()
result2 = user_input()

try:
    result3 = result + result2
except:
    print('Try Again')

print(result3)