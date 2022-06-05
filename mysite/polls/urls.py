from pipes import Template
from re import template
from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('danger/<int:guess>', views.danger, name='dangertest'),
    path('game/<slug:guess>',views.GameView.as_view()),
    path('main/<slug:guess>', views.mainView.as_view(), name = "main"),
    path('redirect', views.redirect, name="redirec"),
]