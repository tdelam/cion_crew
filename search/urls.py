from django.conf.urls import *

urlpatterns = patterns('search.views',
    url(r'^results/$','search', {'template_name': 'search/results.html'}, 'search_results'),
)