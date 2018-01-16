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
>>> baconFile = open('bacon.txt', 'w') # .w method overwrites existing content
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

r       # read - Only allow reading from a file. If it doesn’t exist, there will be an error.
w       # write - Only allow writing to a file. If it doesn’t exist, a new one will be created
a       # append - Append to a file, e.g. write new content after the existing content. If it doesn’t exist, a new one will be created
r+      # read and write - Allow reading and writing to a file.  If it doesn’t exist, there will be an error.
w+      # read and write - Same as r+ but a new file will be created if it doesn’t exist
rb/wb   # binary - Same as r/w but use binary instead of text (Windows only)

f = open(‘questions.txt’)  # Because ‘r’ is used more often than the others, you can use open without the last argument to mean read-only

# WITH - Instead of remembering to close the file, the file is closed automatically when leaving the block of code within the ‘with’ clause.
with open('questions.txt') as f:
    lines = f.readlines()
print lines

# SHUTIL
import shutil, os  # shutil provides functions for copying files and folders
>>> os.chdir('C:\\')
u >>> shutil.copy('C:\\spam.txt', 'C:\\delicious') #(source, destination)
'C:\\delicious\\spam.txt'
v >>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') #if destination is a filename, its used as new name of copied file
'C:\\delicious\\eggs2.txt'

shutil.copy()       #copy a single file     
shutil.copytree()   #copy an entire folder and everything in it
shutil.move()       #move file or folder a path source to destination
os.unlink()         #delete the file at path
os.rmdir()          #delete the folder at path but folder must be empty beforehand
shutil.rmtree()     #delete the folder at path and all files and folders will also be deleted

# Walking A Directory Tree
import os
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')
'The current folder is C:\delicious'  # A string of the current folder’s name
'SUBFOLDER OF C:\delicious: cats'     # A list of strings of the folders in the current folder
'SUBFOLDER OF C:\delicious: walnut'  
'FILE INSIDE C:\delicious: spam.txt'  # A list of strings of the files in the current folder

# ZIP FILES
>>> import zipfile, os
>>> os.chdir('C:\\') #move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.namelist() #returns list of strings for all files and folders contained in zip file.
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt') #.getinfo returns a ZipInfo object about that file
>>> spamInfo.file_size 
13908
>>> spamInfo.compress_size
3828

# Extracting from ZIP files
>>> import zipfile, os
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.extractall()
>>> exampleZip.close()

# Creating and adding to ZIP Files
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
# This code creates new ZIP file called new.zip that has the compressed contents of spam.txt
# Write mode will erase existing contents of a ZIP file
# Use append 'a' to simply add files to existing ZIP file.

Note
# When writing programs that handle files, it’s a good idea to comment out the code that does the actual 
# copy/move/rename/delete and add a print() call instead so you can run the program and verify exactly what it will do.