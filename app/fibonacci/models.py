from math import pow, sqrt
from time import time

from django.db import models


# Create your models here.
def fibonacci(number):
    phi = (1 + sqrt(5)) / 2
    return round(pow(phi, number) / sqrt(5))


def n_fibonacci(number):
    number = int(number)
    return fibonacci(number)
