from django.conf.urls import include, url
from bratzsoft.accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', accounts_views.dashboard, name='dashboard'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^password-reset/$', accounts_views.password_reset, name='password_reset'),
    url(r'^confirm-password/(?P<key>\w+)/$', accounts_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^edit/$', accounts_views.edit, name='edit'),
    url(r'^edit-password/$', accounts_views.edit_password, name='edit_password'),
]
