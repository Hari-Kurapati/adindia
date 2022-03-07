from django.shortcuts import render

# Create your views here.
def company_signin(request):
    return render(request, 'company_signin.html')