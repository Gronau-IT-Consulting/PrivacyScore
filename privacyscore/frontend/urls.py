from django.contrib.auth import views as auth_views
from django.conf.urls import url

from privacyscore.frontend import views

app_name = 'frontend'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^info/$', views.info, name='info'),
    url(r'^legal/$', views.legal, name='legal'),
    url(r'^list/create/$', views.scan_list, name='scan_list'),
    url(r'^list/(?P<scan_list_id>\d+)/$', views.view_scan_list,
        name='view_scan_list'),
    url(r'^list/(?P<scan_list_id>\d+)/scan$', views.scan_scan_list,
        name='scan_scan_list'),
    url(r'^site/(?P<site_id>\d+)/$', views.view_site, name='view_site'),
    url(r'^site/(?P<site_id>\d+)/screenshot$', views.site_screenshot, name='site_screenshot'),
    url(r'^site/(?P<site_id>\d+)/scan/$', views.scan_site, name='scan_site'),
    url(r'^lookup/$', views.lookup, name='lookup'),
    url(r'^scan/$', views.scan, name='scan'),
    url(r'^third_parties/$', views.third_parties, name='third_parties'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='frontend/login.html'), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^user/$', views.user, name='user'),
]
