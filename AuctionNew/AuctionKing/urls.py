from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'account.views.base', name="base"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^products/', include('products.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    ) + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
