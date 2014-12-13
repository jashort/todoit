from django.conf.urls import patterns, url, include
from django.contrib import admin
from todoit import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^items/', include('todo.urls', namespace='todo')),
    url(r'^$', views.index),
)
