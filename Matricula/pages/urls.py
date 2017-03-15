from django.conf.urls import patterns, include, url


urlpatterns = patterns('pages.views',
      url(r'^about', 'about'),
 ) 
