from django.conf.urls import url

from . import views

app_name = 'profile_scraper'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<profile_id>[0-9]+)/$', views.display, name='display'),
]