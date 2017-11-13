from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^plans/$', views.ProductList.as_view()),
    url(r'^payment/$', views.PaymentList.as_view()),
]