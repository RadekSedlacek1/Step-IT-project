from django.shortcuts import render
from first_app.models import Ledger, User


# Create your views here.

def welcome_view(request):
    return render(request, 'first_app/welcome_page.html')

def user_view(request, user_id):
    user = User.objects.id()
    return render(request, 'first_app/user_page.html', context={'user_id': user_id})

def ledger_view(request):
    user_id = User.objects.id()
    ledger_id = Ledger.objects.all()
    context = {'user_id':user_id, 'ledger_id':ledger_id}
    return render(request,'blog/ledger_page.html', context=context)

def expense_view(request):
    return render(request, 'blog/about.html')