# Provides a high-level interface to allow displaying web-based documents to users.
import webbrowser
# Provides a portable way of using operating system dependent functionality.
import os

# Defining function "getStarted."
def getStarted():
    # Calling webbrowser module to open URL: "https://replit.com/~" 
    webbrowser.open("https://replit.com/~", new = 0)
    # Calling webbrowser module to open URL: "https://www.udemy.com/" 
    webbrowser.open("https://www.udemy.com/", new = 0)
    # Calling webbrowser module to open URL: "https://github.com/" 
    webbrowser.open("https://github.com/", new = 0)
    # Calling os module to run VSCode, using it's local path. You will need to find said path, and replace the path specified below for this to function. 
    os.startfile("C:\\Users\\... \\Programs\\Visual Studio Code\\Visual Studio Code.lnk")

# Running function.
getStarted()

# Remember to install pyinstaller and use it to create an executable.
