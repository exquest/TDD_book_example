from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^lists/(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
	url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)

