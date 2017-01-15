from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from adoption import views

urlpatterns = [
    url(r'^ownerlogin/$', views.ownerlogin, name='owner-login'),
    url(r'^adpost/$', views.adpost, name='ad-post'),
    url(r'^adpost/info/$', views.adpostinfo, name='ad-post-info'),
    url(r'^ads/$', views.AdList.as_view(), name='ad-list'),
    url(r'^ads/(?P<pk>[0-9]+)/$', views.AdDetail.as_view(), name='ad-detail'),
    url(r'^owners/$', views.OwnerList.as_view(), name='owner-list'),
    url(r'^owners/(?P<pk>[0-9]+)/$', views.OwnerDetail.as_view(), name='owner-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
