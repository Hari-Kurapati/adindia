from django.shortcuts import render
from django.contrib import messages
from user_signup.models import Users

# Create your views here.
def user_login(request):
    if request.method == "POST":
        user_email = request.POST.get('email')
        user_pass = request.POST.get('password')

        query = f"SELECT * FROM user_signup_users WHERE user_email = '{user_email}' AND user_password = '{user_pass}'"

        t = tuple(Users.objects.raw(query))
        if t==():
            
            messages.success(request, "Incorrect email address or password")
        else:
            return render(request, 'user_purchase.html', {'user': Users.objects.get(user_email=user_email)})

    return render(request, "user_signin.html")