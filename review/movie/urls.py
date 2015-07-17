from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from review.movie import views

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='movie/landing.html'), name='landing'),
    url(r'^(?P<id>\d+)$',views.movie, name='movie'),
    url(r'^(?P<id>\d+)/review/$',views.review, name='review'),
    url(r'^search$',views.search, name='search'),

]
