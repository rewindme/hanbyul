import os.path
from django.conf.urls import *
from bookmarks.views import *
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),'site_media'
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^$', main_page),
    url(r'^user/(\w+)/$',user_page),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$',logout_page),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':site_media}),
    url(r'^register/$',register_page),
    url(r'^register/success/$',TemplateView.as_view(template_name='registration/register_success.html')),
)


