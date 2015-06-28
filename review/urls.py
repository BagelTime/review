from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

import review.movie

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', RedirectView.get_redirect_url(self, 'movie:landing')),
    #url(r'^movies/', include(..movie.urls), namespace='movie'),
    url(r'^movies/', include('review.movie.urls', namespace='movie')),
]
