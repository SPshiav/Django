from django.urls import path,re_path
from app1 import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^train_det', views.train_det, name='train_det'),
    re_path(r'^report', views.report, name='report'),
]