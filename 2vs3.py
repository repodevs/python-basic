# the __future__ module
'''
Ada beberapa syntax pada python3 yang tidak compatible dengan syntax Python2,
contoh module `division`. pada Python2 module ini sudah termasuk built-in module.
tetapi jika ingin menggunakan pada Python3 maka kita harus meng import nya dahulu
'''
from __future__ import division

# ------------------- #

# `print` function
'''
Pada Python3 `print` wajib menggunakan parenthesis `()`
dimana ini hanya menjadi opsional pada Python2
'''

# print "Hello World" # bisa di jalankan pada python2
print ("Hello World")  # pada python3 harus menggunakan parenthesis `()`

'''
Pada function `print` kita dapat langsung untuk menambahkan new line pada akhir secara default.
pada python2 kita bisa menambahkan koma ',' pada akhir untuk membuat baris baru.
tetapi di python3 kita menggunakan parameter `end=" "` untuk menambahkan newline

'''
x = 'Hello newline'
# print x,
print(x, end="  ")

# -------------------- #

# Reading input from keyboard
'''
TL;DR
Python2
`input()` akan menjadikan data sebagai integer jika memasukan integer
`raw_input()` akan menjadikan data sebagai string walaupun memasukan data sebagai integer

>>> x = input('data:')
data:10
>>> x
10
>>> x = input('data:')
data:'10'
>>> x
'10'
>>> x = raw_input('data:')
data:10
>>> x
'10'
>>> x = raw_input('data:')
data:'10'
>>> x
"'10'"
>>>

Python3
`input()` akan menjadikan data sebagai integer
function `raw_input()` sudah tidak ada lagi.

>>> x = input("data:")
data:10
>>> x
'10'
>>> x = input("data:")
data:'10'
>>> x
"'10'"
>>> x = raw_input("data:")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'raw_input' is not defined

'''

# --------------------------------- #

# Integer Division
'''
Pada Python2 hasil akhir dari Division atau pemabagian 2 angka akan dibulatkan
menjadi angka terdekat. contoh 3/2 akan menjadi 1. padahal seharusnya menjadi 1.5
untuk menjadi 1.5 kita harus menambahkan decimal pada salah satu angka tersebut.
misal 3.0/2 = 1.5

Pada Python3 3/2 akan menjadi 1.5 secara default.
'''

# --------------------------------- #

# Unicode Representation
'''
Pada Python2 membutuhkan `u` pada di depan string untuk merubahnya menjadi Unicode
ex: unicode = u'ini adalah unicode'

Pada Python3 string secara default tersimpan menjadi Unicode (utf-8).
'''

# --------------------------------- #

# xrange() Function Removed
'''
Pada Python2 fungsi `range()` mengembalikan sebuah `list`. dan `xrange()` mengembalikan sebuah `objects`

Pada Python3 fungsi `range()` telah dihapus, dan fungsi `xrange()` di rename menjadi `range()`.
Jadi `range()` pada Python3 mengembalikan sebuah `objects`
'''

# --------------------------------- #

# Raise Exception
'''
Pada Python2 bisa menggunakan 2 notations, syntax lama dan syntax baru.
Pada Python3 hanya menerima 1 syntax saja, yaitu syntax baru

>>>
raise IOError, "file error" # <--- Syntax Lama
raise IOError("file error") # <--- Syntax Baru

'''

# --------------------------------- #

# Arguments Exception
'''
Pada Python3 Arguments Exception harus di definisikan sebagai `as` keyword

>>>
except MyError, err: # <------ Python2
except MyError as err: # <---- Python3h
'''

# --------------------------------- #

# 2to3 utility
'''
Pada Python3 terdapat utility untuk convert Python2 code menjadi Python3 code yaitu menggunakan `2to3` utility
ex:

```python2
def area(x, y=3.14):
    a = y*x*x
    print a
    return a

a = area(10)
print "area", a
```

jalankan comman `2to3`
`$2to3 -w py2code.py`
akan menjadi

```
def area(x, y=3.14):
    a = y*x*x
    print(a)
    return a


a = area(10)
print("area", a)
```
'''
