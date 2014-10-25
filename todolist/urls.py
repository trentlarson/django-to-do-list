from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<item_id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<item_id>\d+)/moveup/$', views.moveup, name='moveup'),
    url(r'^(?P<item_id>\d+)/movedown/$', views.movedown, name='movedown'),
)
