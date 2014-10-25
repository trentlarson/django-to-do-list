from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<item_id>\d+)/delete/$', views.delete, name='delete'),
)
