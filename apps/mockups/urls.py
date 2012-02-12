from django.conf.urls.defaults import patterns, url

from .views import MainView

urlpatterns = patterns('',
    url(r'^main/$', MainView.as_view(), name='main'),
)
