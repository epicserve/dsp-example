from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'dsp_example.views.index', {}, 'site_index'),
    (r'^accounts/signin/', 'django.contrib.auth.views.login', {'template_name': 'accounts/signin.html'}, 'signin'),
    (r'^accounts/signout/', 'django.contrib.auth.views.logout_then_login', {}, 'signout'),
    ('^payments/', include('payments.urls'))
)
