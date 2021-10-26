from django.conf.urls import url
from signals_v3 import views

urlpatterns = [
    url('previous/', views.previous_signals_list_view),
    url('', views.signal_list_view, name='signal-list'),
]
