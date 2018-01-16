# File I/O

# On Windows, paths are written using backslashes (\) as the separator between folder names. 
# OS X and Linux, however, use the forward slash (/)as their path separator.
# os.path.join() returns a string with a file path using correct separators
>>> import os
>>> os.path.join('usr', 'bin', 'spam')
'usr\\bin\\spam'

# join names from a list of filenames to the end of a folder’s name:
>>> myFiles = ['accounts.txt', 'details.csv']
>>> for filename in myFiles:
print(os.path.join('C:\\Users\\asweigart', filename))
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv

# You can get the current working directory as a string value 
# with the os.getcwd() function and change it with os.chdir().
>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'

# PATHS - Two way to specify a file path: 
# Absolute: always begins with the root folder
C:\bacon\spam.txt
# Relative: relative to the programs current working directory
.\spam.txt

# Creating new folders
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
# This will create delicious folder and walnut and waffles folder if they dont already exist

# OS.PATH: provides functions for returning absolute path of relative path for checking what path.
os.path.abspath(path) # returns string of the absolute path of an argument
os.path.isabs(path)   # returns True is absolute path, False is relative
os.path.relpath(path, start) # returns a string of a relative path from start path to path
os.path.dirname(path) # returns a string of everything that comes before last slash in path arg
('C:\Windows\System32\calc.exe') # returns C:\Windows\System32
os.path.basename(path) # returns a string of everything that comes after last slash in path arg
('C:\Windows\System32\calc.exe') # returns System32
os.path.split() # if you need dir name and base name together in a tuple value
os.listdir(path) # return lost of filename strings for each file in the path arg
os.path.exists(path) # returns True if file referred to in argument exists
os.path.isfile(path) # returns True if path argument exists AND is a file
os.path.isdir(path)  # returns True if path argument exists ANd is a folder

# To find total size of all files in a directory
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

# Reading & Writing files in Python
>>> baconFile = open('bacon.txt', 'w') # w method overwrites existing content
>>> baconFile.write('Hello world!\n')
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a') # a method appends on to the end of existing text
>>> baconFile.write('Bacon is not a vegetable.')
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read() # open the file in its default read mode
>>> baconFile.close() 
>>> print(content)

.readlines() # gets list of string values from the file, one string for each line of text





