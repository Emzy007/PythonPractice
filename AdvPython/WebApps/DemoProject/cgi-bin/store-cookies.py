#!ENTER SHEBANG HERE PYTHON INTERPRETER
import cgi
from http import cookies

user_details = cookies.SimpleCookie()
#Cookies can be created as key-value pairs
user_details['username'] = ''
user_details['userid'] = 1007

print(user_details.output())#HTTP starts here
print('Content-type:text/html \n') #\n denotes end of HTTP HEADER content