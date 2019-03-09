from math import pow, sqrt
from timeit import default_timer

from django.db import models

# Create your models here.

def n_fibonacci(number):
    start = default_timer()
    number = int(number)
    phi = (1 + sqrt(5)) / 2
    result = round(pow(phi, number) / sqrt(5))
    end = default_timer()
    return result, end-start
