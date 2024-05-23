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
			<h1> Login Form </h1>
			<form method="POST" action="">
				Username : <input type="text" name="username" placeholder="Enter Username" required /> <br />
				Password : <input type="password" name="password" placeholder="Enter Password" required /> <br />
				<input type="submit" name="submit" value ="Login" />
			</form>
		</body>
	</html>
''')


form = cgi.FieldStorage()
if form:
    if('username' in form.keys() and 'password' in form.keys()):
        if(form['username'].value == ''):
            if(form['password'].value == ''):
                print('Login Successful !!! <br /> You will be redirected to homepage in 3 seconds ...')
                print('<meta http-equiv=refresh content="3;url=homepage.py" />')
            else:
                print('Incorrect Password')
        else:
            print('Invalid Username')