
# REGULAR EXPRESSIONS

# Import the regex module with the import re.
import re
# Create a Regex object with the re.compile() function.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
mo = phoneNumRegex.search('My number is 415-555-4242.')
# Call the Match object’s group() method to return a string of the actual matched text.
print('Phone number found: ' + mo.group())

# GROUPING WITH PARENTHESES (mo stands for Match Object)
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'

# | = Pipe character. Used anywhere you want to match one of many expressions
# EG. the regular expression r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
# Can also use pipe to match one of several patterns as part of your regex
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'

# ? = character flags the group before it as an optional part of the pattern.
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'

# * = Match zero or more - the group that precedes the star can occur any number of times in text
>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'

# + = Match one or more
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

# {} = Used if you have a group you want to repeat a specific number of times
(Ha){3,5}
((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

# Greedy and Non-Greedy matching. Regular expressions are greedy by default
# which means that they will match the longest string possible.
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

# The nongreedy version of the curly brackets, which matches the shortest string possible,
# has the closing curly bracket followed by a question mark.
>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'

# findall() method - While search() will return a Match object of the first matched text
# in a string, the findall() method will return the strings of every match in the string.
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
# findall() will return a list of strings as long as there are no groups in the regex.

# When findall() called on regex that has groups, returns a list of tuples of strings
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '1122'), ('212', '555', '0000')]

# SHORTHAND CHARACTER CLASSES
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character.
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character.
# \S Any character that is not a space, tab, or newline.

# [] = Used to define your own character when short-hand ones are too broad

# - = Hyphen used to include a range of letters or numbers
(r'[a-zA-Zo-9]')

# ^ = By putting just after character class's opening bracket - Match all characters that are not in the character class.
(r'[^aeiouAEIOU]')

# ^ = Used at start of regex to indicate match must occur at start of searched text
(r'^Hello')

# $ = Used at end of regex to indicate the string must end with this regex pattern
(r'\d$')

# . = Will match any character except for a newline
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
# Does not include the 'f' in flat becuase the dot only matches one character

# (.*) = stands for anything
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'

# (.*?) = To match any and all text in a nongreedy fashion

# To match everything including the newline character
('.*', re.DOTALL)

# To make your regex xase-insensitive
re.compile(r'robocop', re.I) # or
re.compile(r'robocop', re.IGNORECASE)

# SUMMARY
# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.

# re.VERBOSE - if expression is long, can use multiple lines and ignore whitespace and comments
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')
# Instead of this, can do below
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
\d{3}                           # first 3 digits
(\s|-|\.)                       # separator
\d{4}                           # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)

# If you want to pass multiple options for second argument to regular expression
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)