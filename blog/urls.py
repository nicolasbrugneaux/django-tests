from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import blog.models import Article

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    
	url(r'^faq/$', 'faq'),
    url(r'^contact/$','contact'),
    url(r'^article/(?P<id>\d+)-(?P<slug>[\w\-]+)/$', 'read'),
    url(r'^$', ListView.as_view(model=Article,
    				context_object_name="derniers_articles",
                    template_name="blog/home.html")
    	),

)
