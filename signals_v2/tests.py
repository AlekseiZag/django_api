import random
import os

import signals_v2.models as md

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "almaz_api.config.settings")

import django
django.setup()
from django.core.management import call_command
from signals_v2.views import COLORS
if __name__ == "__main__":
    # md.__dict__.items()
    #
    a = random.choice(COLORS)
    print(a)

