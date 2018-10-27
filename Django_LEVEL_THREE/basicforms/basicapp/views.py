from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def user_view(request):
    form  = forms.UserForm()
    print(request.method)

    if request.method == 'POST':
        print("In post")
        form  = forms.UserForm(request.POST)

    if form.is_valid():
        print("Validation")
        print("Name"+form.cleaned_data['username'])
        print("Email id"+form.cleaned_data['emailid'])
        print("Text"+form.cleaned_data['text'])
    return render(request, 'basicapp/userinfo.html', {'userform': form} )
