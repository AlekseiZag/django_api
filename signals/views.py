from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import string
from random import randint


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


@api_view(['GET'])
def signal_list_view(request):
    data = {}
    value = []
    signals_quantity = randint(5, 25)
    length_of_lst = randint(100, 1000)
    for index in range(signals_quantity):
        for _ in range(length_of_lst):
            level = randint(0, 1)
            value.append(level)
        data[index] = {"id": signals_quantity - index,
                       "name": f'Сигнал {generate_random_string(5) + str(signals_quantity - index)}',
                       "value": value[:]}
        value.clear()
    return JsonResponse(data, safe=False, status=200)
