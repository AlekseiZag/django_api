from django.conf.urls import url
from signals_v2 import views

urlpatterns = [
    url('previous/', views.previous_signals_list_view),
    url('', views.signal_list_view, name='signal-list'),

    # url('^department/([0-9]+)$', views.departmentApi),

]
