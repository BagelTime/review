from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),

                  url(r'^$', RedirectView.as_view(url='/movies/'), name='home'),
                  url(r'^movies/', include('review.movie.urls', namespace='movie')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
