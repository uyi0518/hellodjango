from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.signon, name='signon'),
    url(r'^signin/$', views.signin, name='signin'),
]