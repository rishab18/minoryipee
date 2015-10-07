from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^$','account.views.base', name='base'),
    url(r'^login/$','account.views.handleLogin', name='login'),
    url(r'^signup/$','account.views.handleSignup', name='signup'),
    url(r'^activate/$', 'account.views.activateaccount', name='activate'),
    url(r'^home/$','account.views.home', name='home'),
    #url(r'^add/$','account.views.add', name='add'),
    url(r'^otherhome/$','account.views.otherhome', name='otherhome'),
    url(r'^logout/$','account.views.logoutview', name='logout'),
    url(r'^forgot_password/$', 'account.views.forgot_password', name="forgot_password"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'account.views.reset_password', name='password_reset_confirm'),
    url(r'^search/$', 'account.views.search', name = 'search'),
    url('', include('django.contrib.auth.urls', namespace='auth')),

)


