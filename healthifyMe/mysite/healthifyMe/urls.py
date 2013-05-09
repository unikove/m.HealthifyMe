from django.conf.urls import patterns, url

from healthifyMe import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

