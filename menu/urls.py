from django.conf.urls import patterns, include, url
from django.contrib import admin
from custom_menu import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'menu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*/$', views.all_menu, name='all_menu'),
)
