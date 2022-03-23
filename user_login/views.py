from asyncio import constants
from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

user_email = ''
user_pass = ''

# Create your views here.
def user_login(request):
    global user_email, user_pass
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="R@kib3277", database="adindia")
        cursor = m.cursor()
        d=request.POST
        for key, value in d.items():
            if key == "email":
                user_email = value
            if key == "password":
                user_pass = value
        c = f"select * from users where user_email='{user_email}' and user_password='{user_pass}'"
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.success(request, "Incorrect email address or password")
        else:
            return render(request, 'welcome.html')

    return render(request, "user_signin.html")