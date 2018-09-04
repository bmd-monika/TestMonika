from django.conf.urls import url
from src.snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
]