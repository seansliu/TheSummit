from django.conf.urls import patterns, url
from summit_app import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\w+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\w+)/rate/$', views.rate, name='rate'),
)
