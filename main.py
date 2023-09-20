#What is a list in Python, and how is it different from other data structures like arrays?
    #A list in python is a group of data types such as int's, floats, strings, and other types that are put together
    # by using a [] with as many data types between the brackets as you want seperated by commas
    # EX.
lst = [1,24,"Hi",6,5,76,54,6.532,754,1,1,2,"whats up",4,5,45,4]
# How do you create an empty list in Python?
    #simply create a variable that is equal to [] with nothing inside the brackets
    #EX.
empty_list = []
 #Explain how to add an element to the end of a list in Python.
    #by typing the name of your list then adding .append() will add whatever is in the parentheses to the end of
    #your list whenever the list is printed
    #EX.
empty_list.append("hi")
print(empty_list)
 #How can you access an element at a specific index in a list?
    #to do this, first you print your list, then call the assigneed value in the list.
    #the first value in the list is = to the 0th term of the list. so to call the first value you would type..
print(lst[0])
 #Write a Python code snippet to print all the elements in a list using a for loop.
for number in lst:
    print(number)
 #How do you find the length (number of elements) of a list in Python?p
print(len(lst))
 #Write a Python program to find the sum of all the numbers in a list using a for loop.
numberlist = [1,2,3,4,5]
listsum = 0
for number in numberlist:
    listsum += int(number)
print(listsum)
 #What is a nested for loop, and how can it be used to work with lists of lists in Python?
    #Nested loop ex
nestedloop = [[1,2],[3,4],[5,6],[7,8],[9,10]]
    #nested loops can be used for choosing which elements in a list you want in terms of a larger list