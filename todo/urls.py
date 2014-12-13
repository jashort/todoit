from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from todo import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='list'),
    url(r'add/$', login_required(views.TodoCreate.as_view()), name='add'),
    url(r'(?P<pk>\d+)/$', login_required(views.TodoUpdate.as_view()), name='update'),
    url(r'(?P<pk>\d+)/delete/$', login_required(views.TodoDelete.as_view()), name='delete')
)