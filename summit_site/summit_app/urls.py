from django.conf.urls import patterns, url
from summit_app import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(api/?P<content_id>\w+)/$', views.detail, name='detail'),
    url(r'^(api/?P<content_id>\w+)/results/$', views.results, name='results'),
    url(r'^(api/?P<content_id>\w+)/rate/$', views.rate, name='rate'),
)
