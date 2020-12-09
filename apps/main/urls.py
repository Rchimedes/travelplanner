from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^trippost$', views.trippost),
    url(r'^walldestroy$', views.walldestroy),
    url(r'^(?P<tripid>\d+)$', views.viewtrip),
    url(r'^(?P<tripid>\d+)/addtrip$', views.addtrip),
    url(r'^(?P<tripid>\d+)/edittrip$', views.edittrip),
    url(r'^(?P<tripid>\d+)/update$', views.updatetrip),
    url(r'^(?P<tripid>\d+)/destroytrip$', views.destroytrip),
    url(r'^create$', views.create),
    url(r'^(?P<tripid>\d+)/returntrip$', views.returntrip)
]