import patterns as patterns
from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG and settings.MEDIA_ROOT:
#     urlpatterns += static(settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT)
