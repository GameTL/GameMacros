# Version 3.0 - 2021 September 10

# work for both Mac, Windows, Linux
# use clear() for clearing terminal
# Method 1
# from clearterminal import * -----> clear()
# Method 2
# import clearterminal -----> clearterminal.clear()
import os
import platform
platform = platform.system()
if platform == 'Darwin': # for Unix (MacOS, Linux)
    text = "clear"
elif platform == 'Windows': # for Windows
    text = 'cls'


def clear():
    os.system(text)

if __name__ == '__main__':
    input('''This is the terminal output
This is the terminal output
This is the terminal output
This is the terminal output

Press Enter to excute the clear() function for the terminal

from clearterminal import * -----> clear()
import clearterminal -----> clearterminal.clear()''')
    clear()

