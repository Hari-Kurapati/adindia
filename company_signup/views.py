from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages

cn=""
ac=""
ap=""
email=""
passw=""


# Create your views here.
def signup_comp(request):
    global cn, ac, ap, email, passw
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="R@kib3277",database='adindia')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="company_name":
                cn = value
            if key == "ad_catagory":
                ac = value
            if key == "ad_price":
                ap = value
            if key == "email":
                email = value
            if key == "password":
                passw = value
        c = f"insert into company_singup values (default, '{cn}', '{ac}', '{ap}', '{email}', '{passw}')"
        cursor.execute(c)
        m.commit()
        messages.success(request, 'You are successfully registerted')
    return render(request, "company_signup.html")
