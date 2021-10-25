# API version=2
import numpy as np
from django.shortcuts import redirect
from rest_framework.decorators import api_view
import random
import string
from random import randint
from rest_framework.response import Response
from .models import SignalSet

COLORS = ['navy', 'blue', 'teal', 'aqua', 'green', 'lime', 'olive', 'yellow', 'maroon', 'red', 'purple', 'fuchsia',
          'gray', 'black']


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


@api_view(['GET'])
def previous_signals_list_view(request):
    try:
        qs = SignalSet.objects.first()
        return Response(qs.signals, status=200)
    except AttributeError:
        return redirect('signal-list')


@api_view(['GET'])
def signal_list_view(request):
    value = []
    list_of_signals = []
    signals_quantity = randint(5, 25)
    length_of_lst = randint(100, 1000)
    read_only_values = np.random.choice([True, False], size=(signals_quantity,), p=[1 / 3, 2 / 3])
    for index in range(signals_quantity):
        for _ in range(length_of_lst):
            level = randint(0, 1)
            value.append(level)
        list_of_signals.append({"id": signals_quantity - index,
                                "name": f'Сигнал {generate_random_string(5) + str(signals_quantity - index)}',
                                "readOnly": read_only_values[index],
                                "color": random.choice(COLORS),
                                "value": value[:]})
        value.clear()
    signal_set = SignalSet()
    signal_set.signals = list_of_signals
    signal_set.save()
    if SignalSet.objects.all().count() > 2:
        SignalSet.objects.first().delete()
    return Response(list_of_signals, status=200)
