from django.http import HttpResponse
from django.shortcuts import render

from .number_form import InputField
from .models import n_fibonacci

# Create your views here.
def number(request):
    if request.method == "POST":
        form = InputField(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            return HttpResponse(n_fibonacci(number))
        else:
            return HttpResponse("That doesn't look like a number!")
    elif request.method == "GET":    
        return render(request, 'numbers.html', {'form': InputField()})
