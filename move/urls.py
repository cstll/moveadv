from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from adventures import views as views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  url(r'^adventures', views.adventures, name='adventures'),
  url(r'^packages$', views.packages, name='packages'),
  url(r'^package/((?P<path>.*)$)', views.package, name='package'),
  url(r'^chart', views.chart, name='chart'),
  url(r'^about', views.about, name='about'),
  url(r'^faq', views.faq, name='faq'),
  url(r'^terms', views.terms, name='terms'),
  url(r'^contact', views.contact, name='contact'),
  url(r'^account', views.account, name='account'),
  url(r'^register', views.register, name='register'),
  url(r'^admin', include(admin.site.urls)),
  url(r'^public', include(admin.site.urls)),
  url(r'^public/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.STATIC_ROOT})
)
if settings.DEBUG:
  # static files (images, css, javascript, etc.)
  urlpatterns += patterns('',
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}),
  (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.STATIC_ROOT}))


