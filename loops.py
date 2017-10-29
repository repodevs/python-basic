#!/usr/bin/python3

# --------------- #
# while loops

count = 0
while (count < 9):
    print ('The Count is:', count)
    count = count + 1
print ("Good Bye!")

# using else statements

count = 0
while (count < 5):
    print (count, " is less then 5")
    count = count + 1
else:
    print (count, " is not less then 5")

# using sinle statements

flag = 1
# while (flag): print ('Given flag is really true!')
print ("Good Bye!")



# ----------------- #
# for loops
'''
Syntax:
    for iterating_var in sequence:
        statements(s)


# use `range()` function

>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]

Example:
>>> for var in list(range(5)):
...   print(var)
...
0
1
2
3
4

>>> for letter in 'Python':
...   print ('Current Letter :', letter)
...
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n


>>> fruits = ['banana', 'apple',  'mango']
>>> for fruit in fruits:
...   print ('Current fruit :', fruit)
...
Current fruit : banana
Current fruit : apple
Current fruit : mango

'''



# ----------------------- #
# loops control
'''
## break statement
>>> for letter in 'Python':
...   if letter == 'h':
...     break
...   print ('Letter :', letter)
...
Letter : P
Letter : y
Letter : t


## continue statement
>>> for letter in 'Python':
...   if letter == 'h':
...     continue
...   print ('Letter :', letter)
...
Letter : P
Letter : y
Letter : t
Letter : o
Letter : n


## pass statement
>>> for letter in 'Python':
...   if letter == 'h':
...     pass
...   print ('Letter :', letter)
...
Letter : P
Letter : y
Letter : t
Letter : h
Letter : o
Letter : n

'''
