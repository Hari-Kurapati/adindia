from django.shortcuts import render
from django.contrib import messages
from company_signup.models import Advertisers

# Create your views here.
def company_signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')

        query = f"SELECT * FROM company_signup_advertisers WHERE company_email = '{email}' AND company_password = '{passw}'"

        t = tuple(Advertisers.objects.raw(query))

        if t==():
            messages.success(request, "Incorrect email address or password")
        else:
            print(t)
            return render(request, 'company_product.html', {'company': Advertisers.objects.get(company_email=email)})

    return render(request, 'company_signin.html')