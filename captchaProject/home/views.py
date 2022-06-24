from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import MyForm

def test(request):
    form=MyForm()

    return render(request,'captcha/home.html',{'form':form})

def submit(request):
    if request.method == 'POST':
        form=MyForm(request.POST)
        if form.is_valid():
            name=request.POST['fullname']
            email=request.POST['email']
            print('success')
            print(name)
            print(email)
            return HttpResponse("Thankyou for submiting this form")
        else:
            print('fail')
    return redirect(test)
