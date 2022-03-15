#Problem statement
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.
#
#Code

def likes(names):
    if len(names) == 0:
        return ("no one likes this")
    elif len(names)==1:
        return (str(names[0])+" likes this")
    elif len(names)==2:
        return (str(names[0])+" and "+str(names[1])+" like this")
    elif len(names)==3:
        return (str(names[0])+", "+ str(names[1])+" and " + str(names[2]) + " like this")
    elif len(names) > 3:
        num = len(names) -2
        return (str(names[0])+", "+str(names[1])+" and "+ str(num)+ " others like this")
