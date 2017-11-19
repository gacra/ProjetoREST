from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    return render(request, 'index.html')

@ensure_csrf_cookie
def new_payment(request, plan_id='0'):
    context = {'plan_id': plan_id}
    return render(request, 'new_payment.html', context)