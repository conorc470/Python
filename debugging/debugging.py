# Debugging & Exceptions
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
# Prints: The box using the numbers and characters provided
# Prints: An exception happened: Width must be greater than 2.

# TRACEBACK: include the error message, line number of error and sequence of functionc calls that led to it
# CALL STACK: Sequence of calls
>>> import traceback
>>> try:
        raise Exception('This is the error message.')
    except:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')

# ASSERTION: sanity check to make sure code isnt doing something obviously wrong
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
Traceback (most recent call last):
    File "<pyshell#10>", line 1, in <module>
        assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
# Unlike exceptions, your code should not handle assert statements with try and except 
# If an assert fails, your program should crash.
# Assertions are for programmer errors, not user errors.
# For errors that can be recovered from,raise an exception instead of detecting it with an assert statement.

#LOGGING
import logging
DEBUG -   logging.debug()   #Used for small details.Usually you care about these messages only when diagnosing problems.
INFO  -   logging.info()    #Used to record information on general events in your program or confirm that things are working at their point in the program.
WARNING - logging.warning() #Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
ERROR -   logging.error()   #Used to record an error that caused the program to fail to do something.
CRITICAL- logging.critical()#Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.