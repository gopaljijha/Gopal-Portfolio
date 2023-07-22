from django.shortcuts import render
import mysql.connector as sql
Firstname=''
Lastname=''
Gender=''
Email=''
Password=''
# Create your views here.


def signup_action(request):
    global Firstname, Lastname, Gender, Email, Password
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="dell3567", database="TestEnvironmentProject")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                Firstname = value
            if key == "last_name":
                Lastname = value
            if key == "Gender":
                Gender = value
            if key == "email":
                email = value
            if key == "password":
                password = value
        
        c = "insert into users Values('{}','{}','{}','{}','{}')".format(Firstname, Lastname, Gender, email, password)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')