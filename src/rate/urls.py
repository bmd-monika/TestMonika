from django.conf.urls import url
from src.rate import views

urlpatterns = [
    url(r'^rate/$', view=views.RateView.as_view()),
    url(r'^rate/(?P<id>[\w\-]+)$', views.RateView.as_view()),
]