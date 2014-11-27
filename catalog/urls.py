from django.conf.urls import patterns, url
from catalog import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^category/(?P<category_slug>[-\w]+)/$',views.show_category ),
	url(r'^product/(?P<product_slug>[-\w]+)/$',views.show_product ),
)
