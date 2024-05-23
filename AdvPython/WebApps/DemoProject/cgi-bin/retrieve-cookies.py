import cgi, os
from http import cookies

print('Content-type:text/html \n')

user_details = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
print('User Name: ',user_details['username'].value, '<br />')
print('User ID:', user_details['userid'].value )