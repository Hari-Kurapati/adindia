from django.shortcuts import render
import mysql.connector as sql

user_name = ''
user_phone = ''
user_email = ''
user_pass = ''

# Create your views here.
def signup_user(request):
    global user_name, user_phone, user_email, user_pass
    if request.method == "POST":
        m=sql.connect(host="localhost", user="root", passwd="R@kib3277", database="adindia")
        cursor = m.cursor()
        d=request.POST
        for key, value in d.items():
            if key == "user_name":
                user_name = value
            if key == "email":
                user_email = value
            if key == "phone":
                user_phone = value
            if key == "password":
                user_pass = value
        c = f"insert into users values (default, '{user_name}', '{user_phone}', '{user_email}', '{user_pass}')"
        cursor.execute(c)
        m.commit()
    return render(request, "user_signup.html")