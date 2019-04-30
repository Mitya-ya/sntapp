from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    url(r'home/', views.home, name='home'),
    url(r'payinfo/', views.payinfo, name='payinfo'),
    url(r'directorate/', views.directorate, name='directorate'),
    url(r'new_indications/', views.new_indications, name='new_indications'),
    url(r'snt/', views.snt, name='snt'),
]
