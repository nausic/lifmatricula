from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'main'
urlpatterns = [
   url(r'^$', views.root, name='root'),
   url(r'^about/$', views.about, name='about'),
   url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'},name='login'),
   url(r'^logout/$', auth_views.logout, {'template_name': 'main/logout.html'},name='logout'),
   url(r'^loggedin/$', views.loggedin, name='loggedin'),
   url(r'^register/$', views.register, name='register'),
   url(r'^register/complete/$', views.registration_complete, name='registration_complete'),
   url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'main/password_reset_form.html','post_reset_redirect' : 'mailed/','email_template_name': 'main/password_reset_email.html'},name='password_reset'),
   url(r'^password_reset/mailed/$',auth_views.password_reset_done,{'template_name': 'main/password_reset_done.html'},name='password_reset_done'),
   url(r'^password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,{'template_name': 'main/password_reset_confirm.html','post_reset_redirect' : 'main:password_reset_complete'},name='password_reset_confirm'),
   url(r'^password_reset/complete/$',auth_views.password_reset_complete, {'template_name': 'main/password_reset_complete.html'},name='password_reset_complete'),

 #patterns('main.views',
 #     url(r'', 'root'),
 ]
#(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'
