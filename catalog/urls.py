from django.conf.urls import patterns, url
from catalog import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	# url(r'^category/(?P<category_slug>[-\w]+)/$','show_category', {'template_name':'catalog/category.html'},'catalog_category'),
	# url(r'^category/(<category_slug>)/$',views.show_category, name='catalog_category'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', views.show_category, name='catalog_category'),
	# url(r'^category/(?P<category_name_slug>\w+)/$', views.category, name='category')
	url(r'^product/(<product_slug>)/$',views.show_product ),
)
