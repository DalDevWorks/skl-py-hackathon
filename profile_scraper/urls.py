from django.conf.urls import url

from . import views

app_name = 'profile_scraper'
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^twitter_classifier/$', views.index, name='index'),
    url(r'^lookup/$', views.lookup, name='lookup'),
]