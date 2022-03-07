from django.shortcuts import render

# Create your views here.
def signup_comp(request):
    return render(request, "become_seller.html")