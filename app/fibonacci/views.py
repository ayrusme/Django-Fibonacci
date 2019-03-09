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
            response, time_taken = n_fibonacci(number)
            return HttpResponse('The result is {} \n The time taken is {} seconds'.format(response, time_taken))
        else:
            return HttpResponse("That doesn't look like a number!")
    elif request.method == "GET":    
        return render(request, 'numbers.html', {'form': InputField()})
