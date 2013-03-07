from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
#patterns from blog
urlpatterns += patterns('blog.views',

    url(r'^faq/$', 'faq'),
    url(r'^article/(\d+)/$', 'read'),
    url(r'^article/(\d+)-([\w\-]+)/$', 'read'),
    url(r'^contact/$','contact'),
    url(r'', 'home'),
)