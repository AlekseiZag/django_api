from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.signal_list_view),
]
