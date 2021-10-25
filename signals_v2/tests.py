import random
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "almaz_api.settings")

import django
django.setup()

from signals_v2.views import COLORS

if __name__ == "__main__":
    a = random.choice(COLORS)
    print(a)

