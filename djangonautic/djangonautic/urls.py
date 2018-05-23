
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.home_page),


]

urlpatterns += staticfiles_urlpatterns()