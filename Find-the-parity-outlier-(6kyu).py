#Problem Statment
# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
#The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
#Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
#
#Code

def find_outlier(integers):
    if equal(integers[0], integers[len(integers)-1]) == True:
        return(func(integers[0]%2,integers))
    elif equal(integers[1], integers[2]) == True:
        return(func(integers[2]%2, integers))
def func(x, integers):
    if x == 1:
        for m in range(len(integers)):
            if int(integers[m])%2 == 0:
                return integers[m]
    elif x == 0:
        for m in range(len(integers)):
            if int(integers[m])%2 == 1:
                return integers[m]
def equal(x,y):
    if x%2 == y%2:
        return True
    else:
        return False
