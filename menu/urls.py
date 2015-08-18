from django.conf.urls import patterns, include, url
from django.contrib import admin
from custom_menu import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.all_menu, name='all_menu'),
    url(r'^.*/$', views.all_menu, name='all_menu'),
)
