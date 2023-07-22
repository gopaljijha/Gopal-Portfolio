from django.shortcuts import render
import mysql.connector as sql
Email=''
Password=''
# Create your views here.

# To be deleted
def test_Auth(request):
    return render(request, 'test_Auth.html')


def login_action(request):
    global Email, Password
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="dell3567", database="TestEnvironmentProject")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                email = value
            if key == "password":
                password = value
        
        c = "SELECT * FROM users WHERE email='{}' and password ='{}'".format(email, password)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request, 'basic/index.html')
        

    return render(request, 'login_page.html')