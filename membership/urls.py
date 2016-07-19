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
    url(r'^search/$','phillipo.views.search'),
]
