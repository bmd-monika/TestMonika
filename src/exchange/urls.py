from django.conf.urls import url
from src.exchange import views

urlpatterns = [
    url(r'^exchange/$', view=views.ExchangeView.as_view()),
]