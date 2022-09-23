test = 4
test2 = 'Hello'

try:
    test3 = test + test2
except TypeError:
    print('Can not add a string to a number')
except:
    print('Error')
finally:
    print('okie dokie')
