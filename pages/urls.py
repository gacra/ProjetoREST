from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_payment/$', views.new_payment, name='new_payment'),
    url(r'^new_payment/(?P<plan_id>\d+)/$', views.new_payment, name='new_payment_id')
]