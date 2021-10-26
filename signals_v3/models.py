from django.db import models
from djongo import models as dm


class Signal(models.Model):
    id = models.IntegerField()
    readOnly = models.NullBooleanField()
    isClockSignal = models.NullBooleanField()
    color = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    value = dm.JSONField()

    class Meta:
        abstract = True


class SignalSet(models.Model):
    _id = dm.ObjectIdField()
    signals = dm.ArrayField(model_container=Signal)
    objects = dm.DjongoManager()
