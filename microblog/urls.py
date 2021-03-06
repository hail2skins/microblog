from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from blog.views import blog_list

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^$", blog_list),
    url(r'^admin/', include(admin.site.urls)),
)
