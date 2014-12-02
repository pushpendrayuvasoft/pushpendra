from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from preview.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalog.urls', namespace="catalog")),
    (r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^cart/', include('cart.urls')),

    # url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # url(r'^/', include('catalog.urls', namespace="catalog")),

)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
