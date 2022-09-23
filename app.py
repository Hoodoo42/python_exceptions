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
