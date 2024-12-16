# match is similar to switch in java
# match the op and execute
# Python>3.10
from idlelib.browser import browseable_extension_blocklist


# match variable
#  case pattern 1
#   code block
#    Case pattern 2
#    code block


# write a program to ask a user which browser he want to run the sutomation

browser_name = input("Enter the borwser name :\n")
match browser_name:
    case "firefox":
        print("Starting firefox")
    case "Chrome":
        print("Execute the chrome code")
    case "Edge":
        print("Execute the Edge code")
    case "Safari":
        print("Execute the Safari code")
    case _: # default "_" when nothing match 
        print("Browser not found")
