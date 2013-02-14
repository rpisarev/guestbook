from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import guestbook.settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^([a-z]+)/([a-z]+)/(\d*)/$', 'gba.views.home', name='home'),
	url(r'^([a-z]+)/([a-z]+)/$', 'gba.views.home', name='home'),
	url(r'^(\d*)/$', 'gba.views.home', name='home'),
	url(r'^$', 'gba.views.home', name='home'),
#	{'form_class': RecaptchaForm}
#	url(r'^add/$', 'gba.views.add', name='add'),
    # url(r'^guestbook/', include('guestbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
       (r'^cache/(?P<path>.*)$', 'django.views.static.serve', {
           'document_root': guestbook.settings.MEDIA_ROOT,
           'show_indexes': True,
       }),
   )
