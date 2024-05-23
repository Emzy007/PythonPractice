#!C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310
import cgi, cgitb
#CGITB - CGI Traceback which displays runtime error on the webpage. Shows error type with location.
#If a file name is given then it will not show the error on webpage else output to a file
cgitb.enable(display=0, logdir='AdvPython/WebApps/DemoProject/demoprojlog')

print('Content-type:text/html \n')
print('''
	<html>
		<head>
			<title> My First CGI Script </title>
		</head>
		<body>
			<h1> Hello World </h1>
		</body>
	</html>
''')