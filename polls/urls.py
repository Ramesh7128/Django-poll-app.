from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('polls.views',
    # Examples:
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),

    # Uncomment the next line to enable the admin:
    
)

