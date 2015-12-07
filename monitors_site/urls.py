"""monitors_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from monitors_site import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^details/(?P<hyip_id>.+)/$', views.show_hyip),
    url(r'^search/$', views.search),
    url(r'^search_results/$', views.search_results),
    url(r'^advertise/$', 'advertisements.views.advertise', name='advertise'),
    url(r'^advertise/buy/$', 'advertisements.views.buy_ad', name='buy_ad'),
    url(r'^advertise/(?P<id>.+)/$', 'advertisements.views.preview'),
    url(r'^delete_ad/(?P<ad_id>.+)/$', 'advertisements.views.delete_ad'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)