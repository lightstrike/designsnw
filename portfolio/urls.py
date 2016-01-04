from django.conf.urls import patterns, url

from .views import PortfolioListView, PortfolioDetailView


urlpatterns = patterns('portfolio.views',
    url(r'^$',
        PortfolioListView.as_view(),
        name="list"),
    url(r'^(?P<slug>[\w.,/_\-]+)/$',
        PortfolioDetailView.as_view(),
        name='detail'),
)
