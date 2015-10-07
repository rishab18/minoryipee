from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^upload/$','products.views.uploadProduct', name='upload'),
    url(r'^list/$','products.views.product_list', name ='list'),
    url(r'(?P<id>\d+)/bid/$','products.views.postBid',name = 'bid'),
    url(r'^search_product/$', 'products.views.search_product', name = 'search_product'),
    #url(r'^search/$', 'products.views.search', name = 'search')
)

