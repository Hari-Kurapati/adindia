from django.shortcuts import render
from .models import Users

# Create your views here.
def signup_user(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('email')
        user_phone = request.POST.get('phone')
        user_pass = request.POST.get('password')

        obj = Users(user_name=user_name, user_email=user_email, user_phone=user_phone, user_password=user_pass)
        obj.save()
    return render(request, "user_signup.html")