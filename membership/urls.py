from django.conf.urls import include, url
from django.contrib import admin
from phillipo import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'membership.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','phillipo.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^membersAPI/$',views.ListMembers.as_view()),
    url(r'^members/$','phillipo.views.showMembers'),
    url(r'^members/(?P<month>[\w\-]+)/$','phillipo.views.memberMonth'),
    url(r'^search/$','phillipo.views.search'),
    url(r'^search/(?P<query>[\w\-]+)/$','phillipo.views.searchq'),
    url(r'^register/$','phillipo.views.register'),
]
